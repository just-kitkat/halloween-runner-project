import random
from typing import Type
import math

class Weapon:
    def __init__(self, data: dict):
        self.damage = data["damage"]
        #accuracy is a integer from 1-100, acts as percentage chance of missing
        self.accuracy = data["accuracy"]
        self.durability = data["durability"]
        self.name = data["name"]
        self.description = data["description"]
        
    #generalised for both enemies and the player
    def attack(self, entity_attacked,protection_val = 0):
        if random.randint(1,100)>self.accuracy:
            #attack missed
            return [False,0]
        else:
            #attack hit
            if self.damage == 1:
                entity_attacked.reduce_health(self.damage)
                return [True,self.damage,0]
            else:
                true_damage = math.floor(self.damage*(1-(protection_val/100)))
                entity_attacked.reduce_health(true_damage)
                return [True,true_damage,self.damage-true_damage]

weapon_data = {
    "fists": {
        "name": "My Fists",
        "damage": 1,
        "accuracy": 90,
        "durability": None,
        "description": "Very low damage"
    },
    "wooden spear": {
        "name": "Wooden Spear",
        "damage": 3,
        "accuracy": 85,
        "durability": None,
        "description": "Low damage"
    },
    "wooden sword": {
        "name": "Wooden Sword",
        "damage": 3,
        "accuracy": 85,
        "durability": None,
        "description": "Low damage"
    },
    "cutlery dagger": {
        "name": "Cultery Dagger",
        "damage": 2,
        "accuracy": 85,
        "durability": None,
        "description": "Very low damage"
    },
    "crude bow": {
        "name": "Crude Bow",
        "damage": 2,
        "accuracy": 80,
        "durability": None,
        "description": "Very low damage"
    },
    "silver sword": {
        "name": "Silver Sword",
        "damage": 5,
        "accuracy": 90,
        "durability": None,
        "description": "High damage"
    },
    "ornate dagger":{
        "name":"Ornate Dagger",
        "damage":4,
        "accuracy":85,
        "durability": None,
        "description": "High damage"
    },
    "magic staff":{
        "name":"Magic Staff",
        "damage":2,
        "accuracy":95,
        "durability": None,
        "description": "Very low damage"
    },
    "claws":{
        "name":"Claws",
        "damage":3,
        "accuracy":95,
        "durability": None,
        "description": "Low damage"
    },
    "cane":{
        "name":"Mother's Cane",
        "damage":3,
        "accuracy":100,
        "durability": None,
        "description": "Low damage"
    },
    "slipper":{
        "name":"Mother's Slipper",
        "damage":2,
        "accuracy":100,
        "durability": None,
        "description": "Very low damage"
    },
    "belt":{
        "name":"Father's Belt",
        "damage":7,
        "accuracy":50,
        "durability": None,
        "description": "HIGH damage"
    },
    "taxes":{
        "name":"Father's Taxes",
        "damage":6,
        "accuracy":50,
        "durability": None,
        "description": "HIGH damage"
    },
    "horseman head":{
        "name":"Horseman's Head",
        "damage":4,
        "accuracy":90,
        "durability": None,
        "description": "High damage"
    },
    "mega sword":{
        "name":"Fiery Sword",
        "damage":random.randint(10,15),
        "accuracy":75,
        "durability": None,
        "description": "The boss's sword. Its big, its scary, and it hurts..."
    }
}

def create_weapon(label: str) -> Weapon:
    data = weapon_data[label]
    return Weapon(data)

def create_random_weapon() -> Weapon:
    weapon = random.choice(all_weapons())
    return create_weapon(weapon)

def all_weapons():
    return list(weapon_data.keys())
