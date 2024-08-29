"""combat.py

Base classes and helper functions for combat implementation.
"""
import math
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


class StrikeResult:

    def __init__(
        self,
        attacker_name: str,
        attacker_weapon: str,
        defender_name: str,
        defender_weapon: str,
        hit: bool,
        damage: int,
        reduction: int,
    ):
        self.attacker_name = attacker_name
        self.attacker_weapon = attacker_weapon
        self.defender_name = defender_name
        self.defender_weapon = defender_weapon
        self.hit = hit
        self.damage = damage
        self.reduction = reduction


class Battle:

    def __init__(self, fighter1: Combatant, fighter2: Combatant):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def is_ended(self) -> bool:
        """Battle ends when either fighter dies."""
        return self.fighter1.is_dead() or self.fighter2.is_dead()

    def strike(self, attacker: Combatant, defender: Combatant) -> StrikeResult:
        """A single blow by an attacker to a defender."""
        if random.randint(1, 100) > attacker.accuracy():
            #attack missed
            return StrikeResult(
                attacker_name=attacker.name,
                attacker_weapon=attacker.weapon.name,
                defender_name=defender.name,
                defender_weapon=defender.weapon.name,
                hit=False,
                damage=0,
                reduction=0,
            )
        #attack hit
        damage = attacker.damage()
        if damage == 1:
            reduction = 0
        else:
            reduction = math.ceil(damage * defender.defense() / 100)
        return StrikeResult(
            attacker_name=attacker.name,
            attacker_weapon=attacker.weapon.name,
            defender_name=defender.name,
            defender_weapon=defender.weapon.name,
            hit=True,
            damage=damage,
            reduction=reduction,
        )

    def exchange(self) -> list[StrikeResult]:
        """A single exchange of attacks between the two fighters.
        Returns the result of the exchange, as a list of StrikeResults.
        """
        results = []
        # Fighter 1 goes first
        result = self.strike(self.fighter1, self.fighter2)
        if result.hit:
            self.fighter2.reduce_health(result.damage - result.reduction)
        results.append(result)
        if self.is_ended():
            return results

        # Fighter2 goes next
        result = self.strike(self.fighter2, self.fighter1)
        if result.hit:
            self.fighter1.reduce_health(result.damage - result.reduction)
        results.append(result)
        return results


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
