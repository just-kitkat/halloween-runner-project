import random

import data

weapon_data = data.load("weapon.json")


class Weapon:

    def __init__(self, data: dict):
        self.damage = data["damage"]
        #accuracy is a integer from 1-100, acts as percentage chance of missing
        self.accuracy = data["accuracy"]
        self.durability = data["durability"]
        self.name = data["name"]
        self.description = data["description"]

    def info(self) -> str:
        infostr = ""
        infostr += f"Name: {self.name}"
        infostr += f"Damage: {self.damage}"
        infostr += f"Accuracy: {self.accuracy}"
        infostr += "\n"
        infostr += f"{self.description}"
        return infostr


def create_weapon(label: str) -> Weapon:
    data = weapon_data[label]
    return Weapon(data)

def create_random_weapon() -> Weapon:
    weapon = random.choice(all_weapons())
    if weapon == "mega sword":  # not obtainable by player, belongs only to the boss.
        weapon = "belt"
    return create_weapon(weapon)

def all_weapons():
    return list(weapon_data.keys())
