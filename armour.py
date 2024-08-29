import random

import data

armor_data = data.load("armor.json")


class Armor:

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


def create_armor(label: str) -> Armor:
    data = armor_data[label]
    return Armor(data)


def create_random_armor() -> Armor:
    armor = random.choice(all_armor())
    return create_armor(armor)


def all_armor():
    return list(armor_data.keys())
