import random

import data

food_data = data.load("food.json")
weapon_data = data.load("weapon.json")
armor_data = data.load("armor.json")


class Item:
    """Superclass for all items in the game."""
    type = "item"

    def __init__(self, name: str):
        self.name = name

    def info(self) -> str:
        infostr = f"Name: {self.name}"
        return infostr


class Armor(Item):
    type = "armor"

    def __init__(self, data):
        super().__init__(data["name"])
        self.protection = data["protection"]
        self.durability = data["durability"]
        self.description = data["description"]

    def info(self) -> str:
        infostr = super().info()
        infostr += f"Protection: {self.protection}"
        infostr += "\n"
        infostr += self.description
        return infostr


class Food(Item):
    type = "food"

    def __init__(self, name: str, health: int):
        super().__init__(name)
        self.health = health


class Weapon(Item):
    type = "weapon"

    def __init__(self, data: dict):
        super().__init__(data["name"])
        self.damage = data["damage"]
        self.accuracy = data["accuracy"]
        self.durability = data["durability"]
        self.description = data["description"]

    def info(self) -> str:
        infostr = super().info()
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
