import random

import data

food_data = data.load("food.json")
weapon_data = data.load("weapon.json")
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


class Food:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def info(self) -> str:
        return ""


class Weapon:

    def __init__(self, data: dict):
        self.name = data["name"]
        self.damage = data["damage"]
        self.accuracy = data["accuracy"]
        self.durability = data["durability"]
        self.description = data["description"]

    def info(self) -> str:
        infostr = ""
        infostr += f"Name: {self.name}"
        infostr += f"Damage: {self.damage}"
        infostr += f"Accuracy: {self.accuracy}"
        infostr += "\n"
        infostr += f"{self.description}"
        return infostr


def all_armor():
    return list(armor_data.keys())


def all_food():
    return list(food_data.keys())


def all_weapons():
    return list(weapon_data.keys())


def create_armor(label: str) -> Armor:
    data = armor_data[label]
    return Armor(data)


def create_food(data: dict) -> Food:
    return Food(data["name"], data["health"])


def create_weapon(label: str) -> Weapon:
    data = weapon_data[label]
    return Weapon(data)


def random_armor() -> Armor:
    armor = random.choice(all_armor())
    return create_armor(armor)


def random_food() -> Food:
    return create_food(random.choice(all_food()))


def random_weapon() -> Weapon:
    weapon = random.choice(
        [name for name in all_weapons() if name != "mega sword"])
    return create_weapon(weapon)
