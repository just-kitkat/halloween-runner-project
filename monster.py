import random
from weapon import create_weapon

def monster_name_generation():
    first_name = ['Grim', 'Mortis', 'Thorne', 'Vex', 'Hex', 'Nyx', 'Dread', 'Wraith', 'Shade', 'Gloom', 'Ethan', 'Seah', 'Joshua', 'Wong', 'Cho']
    last_name = ['Nightshade', 'Bloodbane', 'Frostmourne', 'Grimspike', 'Darkwhisper', 'Deathclaw', 'Skullrend', 'Shadowfang', 'Wraithborn', 'Ironshade', 'Wang', 'Eket', 'Zijia', 'Zin']
    lenf = len(first_name)
    lenl = len(last_name)
    num1 = random.randint(0, lenf-1)
    num2 = random.randint(0, lenl-1)
    monster_name = f'{first_name[num1]} {last_name[num2]}'
    return monster_name

class Monster:
    def __init__(self,monster_data):
        self.name = monster_name_generation()
        self.weapon = create_weapon(random.choice(monster_data["weapon_label"]))
        self.health = monster_data["health"]
        self.type = monster_data["type"]

    #damage is done inside weapon class
    def monster_attack_player(self,player):
        bool = self.weapon.attack(player)
        if bool:
            print(f"{self.name}\'s attack hit,[ {self.weapon.damage}] damage dealt")
        else:
            print(f"{self.name}\'s attack missed!")

    def player_attack_monster(self,player):
        bool = player.weapon.attack(self)
        if bool:
            print(f"{player.name}\'s attack hit,[ {self.weapon.damage}] damage dealt")
        else:
            print(f"{player.name}\'s attack missed!")

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

monster_data = {
    "skeleton":{
        "type":"Skeleton",
        "health": 3,
        "weapon_label":["fists","crude bow","crude bow","cutlery dagger"]
    },
    "zombie":{
        "type":"Zombie",
        "health":5,
        "weapon_label":["fists","cutlery dagger","wooden spear","wooden sword"]
    },
    "vampire":{
        "type":"Vampire",
        "health":6,
        "weapon label":["wooden sword","wooden sword","cutlery dagger"]
    },
    "ghost":{
        "type":"Ghost",
        "health":2,
        "weapon label":["fists","fists","cutlery dagger"]
    }
}

def create_monster(label: str) -> Monster:
    data = monster_data[label]
    return Monster(data)

def all_monsters():
    return monster_data.keys()