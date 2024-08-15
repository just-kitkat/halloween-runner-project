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
        "accuracy": 75,
        "durability": None,
        "description": "[placeholder]"
    },
    "wooden spear": {
        "name": "Wooden Spear",
        "damage": 3,
        "accuracy": 90,
        "durability": None,
        "description": "[placeholder]"
    },
    "wooden sword": {
        "name": "Wooden Sword",
        "damage": 3,
        "accuracy": 90,
        "durability": None,
        "description": "[placeholder]"
    },
    "cutlery dagger": {
        "name": "Cultery Dagger",
        "damage": 2,
        "accuracy": 80,
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
    }
}

def create_weapon(label: str) -> Weapon:
    data = weapon_data[label]
    return Weapon(data)

def all_weapons():
    return list(weapon_data.keys())
