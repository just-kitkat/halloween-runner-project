import random

import data
from weapon import create_weapon

monster_data = data.load("monster.json")
boss_data = monster_data.pop("boss")
min_, max_ = boss_data["health"]
boss_data["health"] = random.randint(min_, max_)
names = data.load("names.json")
first_names = names["first_names"]
last_names = names["last_names"]


def monster_name_generation():
    lenf = len(first_names)
    lenl = len(last_names)
    num1 = random.randint(0, lenf - 1)
    num2 = random.randint(0, lenl - 1)
    monster_name = f'{first_names[num1]} {last_names[num2]}'
    return monster_name


class Monster:

    def __init__(self, data, boss=False):
        self.name = monster_name_generation()
        if boss:
            self.name = "The Ghost King"
        self.weapon = create_weapon(random.choice(data["weapon label"]))
        self.health = data["health"]
        self.type = data["type"]

    #damage is done inside weapon class
    def monster_attack_player(self, player):
        lst = self.weapon.attack(player, player.armor.protection)
        bool = lst[0]
        if bool:
            print(
                f"{self.name}\'s attacked you with \"{self.weapon.name}\", dealing {lst[1]} damage"
            )
            if lst[2] != 0:
                print(f"Your armour protected you from {lst[2]} damage!")
        else:
            print(f"{self.name}\'s attack missed!")
        print("Your health:", max(0, player.get_health()))

    def player_attack_monster(self, player):
        lst = player.weapon.attack(self)
        bool = lst[0]
        if bool:
            print(
                f"You attacked {self.name} with \"{player.weapon.name}\", dealing {lst[1]} damage."
            )
        else:
            print("Your attack missed!")
        print(f"{self.name}'s health:", max(0, self.get_health()))

    def reduce_health(self, hp):
        self.health -= hp

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_type(self):
        return self.type


def create_monster(label: str) -> Monster:
    data = monster_data[label]
    return Monster(data)


def create_random_monster() -> Monster:
    monster = random.choice(all_monsters())
    return create_monster(monster)


def create_boss() -> Monster:
    return Monster(boss_data, boss=True)


def all_monsters():
    return list(monster_data.keys())


# Testing, do not delete.
if __name__ == "__main__":
    print(list(monster_data.keys()))
    entity = create_monster("ghost")
    print(entity.weapon.name)
