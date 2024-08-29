import random

from combat import Combatant
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


class Monster(Combatant):

    def __init__(self, data, boss=False):
        super().__init__(monster_name_generation(), data["health"])
        if boss:
            self.name = "The Ghost King"
        self.weapon = create_weapon(random.choice(data["weapon label"]))
        self.type = data["type"]


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
