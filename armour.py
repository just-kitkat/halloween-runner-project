import random


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


armour_data = {
    "leather": {
        "name":
        "Leather Tunic",
        "protection":
        20,
        "durability":
        None,
        "description":
        "A very very old piece of leather. Seems to belong to some sort of servant..."
    },
    "chainmail": {
        "name": "Chainmail Tunic",
        "protection": 30,
        "durability": None,
        "description": "Used to be bling bling shiny. Lightweight but useful."
    },
    "iron": {
        "name":
        "Iron Breastplate",
        "protection":
        50,
        "durability":
        None,
        "description":
        "This massive piece of armour will protect you from the worst of hits..."
    },
    "": {
        "name": "Iron helmet",
        "protection": 10,
        "durability": None,
        "description": "This head gear will serve you well"
    },
    "white tshirt": {
        "name":
        "White T-shirt",
        "protection":
        0,
        "durability":
        None,
        "description":
        "This fancy piece of fabric provides warmth from the cold, but no combat protection at all..."
    },
}


def create_armour(label: str) -> Armour:
    data = armour_data[label]
    return Armour(data)


def create_random_armour() -> Armour:
    armour = random.choice(all_armour())
    return create_armour(armour)


def all_armour():
    return list(armour_data.keys())


"""
Class helmet
reduces crit chance
Class chestplate
dmg reduction
Class leggings
dmg reduction
Class boots
more number of moves, "agility"
"""
