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


weapon_data = {
    "fists": {
        "name":
        "My Fists",
        "damage":
        1,
        "accuracy":
        90,
        "durability":
        None,
        "description":
        "When you clench your fists, they seem to radiate a faint, almost imperceptible glow, hinting at the raw energy contained within."
    },
    "wooden spear": {
        "name":
        "Wooden Spear",
        "damage":
        3,
        "accuracy":
        85,
        "durability":
        None,
        "description":
        "This wooden spear is a simple yet effective weapon, crafted from a sturdy oak shaft. The spearhead, though unadorned, is sharp and pointed, fashioned from metal or hardened stone. The wood is polished but retains a natural grain, giving it a rustic appearance."
    },
    "wooden sword": {
        "name":
        "Wooden Sword",
        "damage":
        3,
        "accuracy":
        85,
        "durability":
        None,
        "description":
        "This wooden sword is a basic yet functional training weapon, crafted from a single piece of sturdy, polished wood. Its blade is flat and wide, resembling a crude version of a more refined sword, with no sharp edges but a solid, imposing presence."
    },
    "cutlery dagger": {
        "name":
        "Cultery Dagger",
        "damage":
        2,
        "accuracy":
        85,
        "durability":
        None,
        "description":
        "This dagger, originally designed as a piece of cutlery, has been adapted into a surprisingly functional weapon. The blade, though short and slender, retains a keen edge, suitable for swift and precise strikes."
    },
    "crude bow": {
        "name":
        "Crude Bow",
        "damage":
        2,
        "accuracy":
        80,
        "durability":
        None,
        "description":
        "This crude bow is a rugged and makeshift weapon, fashioned from a flexible yet resilient branch or piece of raw wood. Its design is simplistic, with minimal craftsmanship evident in its construction."
    },
    "silver sword": {
        "name":
        "Silver Sword",
        "damage":
        5,
        "accuracy":
        90,
        "durability":
        None,
        "description":
        "This elegant sword boasts a blade forged from gleaming silver, giving it a distinctive, lustrous sheen. The metal is meticulously polished, reflecting light with a brilliant sheen that hints at its magical or ceremonial significance."
    },
    "ornate dagger": {
        "name":
        "Ornate Dagger",
        "damage":
        4,
        "accuracy":
        85,
        "durability":
        None,
        "description":
        "This exquisite dagger is a masterwork of craftsmanship and artistry. The blade, though short and sleek, is intricately engraved with delicate patterns and symbols, suggesting both a decorative and functional purpose."
    },
    "magic staff": {
        "name":
        "Magic Staff",
        "damage":
        2,
        "accuracy":
        95,
        "durability":
        None,
        "description":
        "This magic staff is a slender, elegantly carved piece of wood or metal, imbued with arcane energy. While the staff is not designed for combat, it can deliver some deadly blows!"
    },
    "claws": {
        "name":
        "Claws",
        "damage":
        3,
        "accuracy":
        95,
        "durability":
        None,
        "description":
        "These formidable claws are a set of metal or bone implements designed to be worn over your hands like gauntlets."
    },
    "cane": {
        "name":
        "Mother's Cane",
        "damage":
        3,
        "accuracy":
        100,
        "durability":
        None,
        "description":
        "This cane is a cherished heirloom, imbued with sentimental value and a subtle aura of magic. This piece of plastic has caused generations of pain and suffering."
    },
    "slipper": {
        "name":
        "Mother's Slipper",
        "damage":
        2,
        "accuracy":
        100,
        "durability":
        None,
        "description":
        "This seemingly ordinary slipper is imbued with a comforting, almost magical essence. Crafted from soft, durable fabric, it will certainly deliver a hefty blow to enemies (or your children)..."
    },
    "belt": {
        "name":
        "Father's Belt",
        "damage":
        7,
        "accuracy":
        50,
        "durability":
        None,
        "description":
        "This rugged and practical belt is crafted from high-quality, durable leather. It is a highly effective weapon to combat any disobedience."
    },
    "taxes": {
        "name":
        "Father's Taxes",
        "damage":
        6,
        "accuracy":
        50,
        "durability":
        None,
        "description":
        "This peculiar item is not a weapon or piece of gear but rather a collection of meticulously organized documents and scrolls. Bound in a leather folder or case, Father's Taxes consists of detailed records, financial ledgers, and various receipts. It's sheer weight will deal massive damage to anyone unfortunate enough to be crushed under it."
    },
    "horseman head": {
        "name":
        "Horseman's Head",
        "damage":
        4,
        "accuracy":
        90,
        "durability":
        None,
        "description":
        "The head is also rumored to have a protective enchantment, warding off enemies."
    },
    "mega sword": {
        "name":
        "Fiery Sword",
        "damage":
        random.randint(10, 15),
        "accuracy":
        75,
        "durability":
        None,
        "description":
        "This blazing sword is a spectacular weapon, with a blade forged from a rare, heat-resistant metal that seems to flicker and dance with internal flames. The blade is imbued with a constant, magical fire, casting a warm, flickering glow that illuminates the surroundings. The fire does not consume the metal but instead is contained within an intricate pattern of runes along the length of the blade. It's big, scary, and it hurts..."
    }
}


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
