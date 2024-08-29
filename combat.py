"""combat.py

Base classes and helper functions for combat implementation.
"""
import random

import data
import item

monster_data = data.load("monster.json")
boss_data = monster_data.pop("boss")
min_, max_ = boss_data["health"]
boss_data["health"] = random.randint(min_, max_)
names = data.load("names.json")
first_names = names["first_name"]
last_names = names["last_name"]


class Combatant:
    """Superclass for all entities engaging in combat."""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None
        self.armor = None

    def get_health(self):
        return self.health

    def reduce_health(self, hp):
        # Health is allowed to drop below 0.
        self.health -= hp

    def add_health(self, hp):
        # No upper limit to combatant health.
        self.health += hp

    def is_dead(self) -> bool:
        return self.health <= 0

    def accuracy(self) -> int:
        """accuracy is a integer from 1-100,
        acts as percentage chance of missing.
        """
        return self.weapon.accuracy if self.weapon else 0

    def damage(self) -> int:
        """Damage dealt to enemy"""
        return self.weapon.damage if self.weapon else 0

    def defense(self) -> int:
        """Damage reduction"""
        return self.armor.protection if self.armor else 0


class Monster(Combatant):

    def __init__(self, name: str, health: int, type: str):
        super().__init__(name, health)
        self.type = type


class Player(Combatant):

    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        self.items = []
        self.armor = None
        self.weapon = None

    def take_item(self, item):
        self.items.append(item)

    def unequip_armor(self) -> None:
        if self.armor:
            self.items.append(self.armor)
        self.armor = None

    def unequip_weapon(self) -> None:
        if self.weapon:
            self.items.append(self.weapon)
        self.weapon = None

    def equip_item(self, item_) -> None:
        if isinstance(item_, item.Weapon):
            self.unequip_weapon()
            self.weapon = item_
        elif isinstance(item_, item.Armor):
            self.items.append(self.armor)
            self.armor = item_
        else:
            pass




def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f'{first_name} {last_name}'

def create_player(name: str) -> Player:
    player = Player(name=name, health=100)
    player.equip_item(item.create_weapon("fists"))
    player.equip_item(item.create_armor("white tshirt"))
    return player

def create_monster(data: dict, boss=False) -> Monster:
    if boss:
        name = "The Ghost King"
    else:
        name = generate_name()
    monster = Monster(name, data["health"], data["type"])
    monster.weapon = item.create_weapon(random.choice(data["weapon label"]))
    return monster

def create_random_monster() -> Monster:
    monster = random.choice(all_monsters())
    return create_monster(monster)

def create_boss() -> Monster:
    return create_monster(boss_data, boss=True)

def all_monsters():
    return list(monster_data.keys())


# Testing, do not delete.
if __name__ == "__main__":
    print(list(monster_data.keys()))
    entity = create_monster("ghost")
    print(entity.weapon.name)
