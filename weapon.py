import random
from typing import Type

class Weapon:
    def __init__(self, data: dict):
        self.damage = data["damage"]
        #accuracy is a integer from 1-100, acts as percentage chance of missing
        self.accuracy = data["accuracy"]
        self.durability = data["durability"]
        self.name = data["name"]
        self.description = data["description"]
    #generalised for both enemies and the player
    def attack(self,entity):
        if random.randint(1,100)>self.accuracy:
            #attack missed
            return False
        else:
            #attack hit
            #might want to have a block function for the player, give a % reduction in dmg with the cost of a turn, need to modify damage taken
            entity.reduce_health(self.damage)
            return True

weapon_data = {
    "fists": {
        "name": "My Fists",
        "damage": 1,
        "accuracy": 90,
        "durability": None,
        "description": "[placeholder]"
    },
    "wooden spear": {
        "name": "Wooden Spear",
        "damage": 3,
        "accuracy": 85,
        "durability": None,
        "description": "[placeholder]"
    },
    "wooden sword": {
        "name": "Wooden Sword",
        "damage": 3,
        "accuracy": 85,
        "durability": None,
        "description": "[placeholder]"
    },
    "cutlery dagger": {
        "name": "Cultery Dagger",
        "damage": 2,
        "accuracy": 85,
        "durability": None,
        "description": "[placeholder]"
    },
    "crude bow": {
        "name": "Crude Bow",
        "damage": 2,
        "accuracy": 80,
        "durability": None,
        "description": "[placeholder]"
    },
    "silver sword": {
        "name": "Silver Sword",
        "damage": 5,
        "accuracy": 90,
        "durability": None,
        "description": "[placeholder]"
    },
    "ornate dagger":{
        "name":"Ornate Dagger",
        "damage":4,
        "accuracy":85,
        "durability": None,
        "description": "[placeholder]"
    },
    "magic staff":{
        "name":"Magic Staff",
        "damage":2,
        "accuracy":95,
        "durability": None,
        "description": "[placeholder]"
    },
    "claws":{
        "name":"Claws",
        "damage":3,
        "accuracy":95,
        "durability": None,
        "description": "[placeholder]"
    },
    "cane":{
        "name":"Mother's Cane",
        "damage":3,
        "accuracy":100,
        "durability": None,
        "description": "[placeholder]"
    },
    "slipper":{
        "name":"Mother's Slipper",
        "damage":2,
        "accuracy":100,
        "durability": None,
        "description": "[placeholder]"
    },
    "belt":{
        "name":"Father's Belt",
        "damage":7,
        "accuracy":50,
        "durability": None,
        "description": "[placeholder]"
    },
    "taxes":{
        "name":"Father's Taxes",
        "damage":6,
        "accuracy":50,
        "durability": None,
        "description": "[placeholder]"
    },
    "horseman head":{
        "name":"Horseman's Head",
        "damage":4,
        "accuracy":90,
        "durability": None,
        "description": "[placeholder]"
    },
}

def create_weapon(label: str) -> Weapon:
    data = weapon_data[label]
    return Weapon(data)

def create_random_weapon() -> Weapon:
    weapon = random.choice(all_weapons())
    return create_weapon(weapon)

def all_weapons():
    return list(weapon_data.keys())
