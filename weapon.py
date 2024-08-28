import random
import math

import data


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

    #generalised for both enemies and the player
    def attack(self, entity_attacked, protection_val=0):
        if random.randint(1, 100) > self.accuracy:
            #attack missed
            return [False, 0]
        else:
            #attack hit
            if self.damage == 1:
                entity_attacked.reduce_health(self.damage)
                return [True, self.damage, 0]
            else:
                actual_damage = math.floor(self.damage *
                                           (1 - (protection_val / 100)))
                entity_attacked.reduce_health(actual_damage)
                return [True, self.damage, self.damage - actual_damage]


weapon_data = data.load("weapon.json")


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
