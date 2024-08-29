import random

import data

armour_data = data.load("armor.json")


class Armour:

    def __init__(self, data):
        self.name = data["name"]
        self.protection = data["protection"]
        self.durability = data["durability"]
        self.description = data["description"]

    def info(self) -> str:
        infostr = ""
        infostr += f"Name: {self.name}"
        infostr += f"Protection: {self.protection}"
        infostr += "\n"
        infostr += self.description
        return infostr


def create_armour(label: str) -> Armour:
    data = armour_data[label]
    return Armour(data)


def create_random_armour() -> Armour:
    armour = random.choice(all_armour())
    return create_armour(armour)


def all_armour():
    return list(armour_data.keys())
