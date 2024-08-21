import random
from weapon import create_random_weapon

def monster_name_generation():
    first_name = ['Grim', 'Mortis', 'Thorne', 'Vex', 'Hex', 'Nyx', 'Dread', 'Wraith', 'Shade', 'Gloom', 'Ethan', 'Seah', 'Joshua', 'Wong', 'Cho']
    last_name = ['Nightshade', 'Bloodbane', 'Frostmourne', 'Grimspike', 'Darkwhisper', 'Deathclaw', 'Skullrend', 'Shadowfang', 'Wraithborn', 'Ironshade', 'Wang', 'Zijia', 'Zin']
    lenf = len(first_name)
    lenl = len(last_name)
    num1 = random.randint(0, lenf-1)
    num2 = random.randint(0, lenl-1)
    monster_name = f'{first_name[num1]} {last_name[num2]}'
    return monster_name

class Monster:
    def __init__(self,data):
        self.name = monster_name_generation()
        self.weapon = create_random_weapon()
        self.health = data["health"]
        self.type = data["type"]

    #damage is done inside weapon class
    def monster_attack_player(self, player):
        lst = self.weapon.attack(player,player.armor.protection)
        bool = lst[0]
        if bool:
            print(f"{self.name}\'s attack hit, {lst[1]} damage dealt ({lst[2]} dmg. blk.)")
            print("Monster's health:", self.get_health())
        else:
            print(f"{self.name}\'s attack missed!")

    def player_attack_monster(self, player):
        lst = player.weapon.attack(self)
        bool = lst[0]
        if bool:
            print(f"{player.name}\'s attack hit, {lst[1]} damage dealt ({lst[2]} dmg. blk.)")
            print("Player's health:", player.get_health())
        else:
            print(f"{player.name}\'s attack missed!")

    def reduce_health(self, hp):
        self.health -= hp

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_type(self):
        return self.type


monster_data = {
    "skeleton":{
        "type":"Skeleton",
        "health": 3,
        "weapon_label":["fists","crude bow","crude bow","cutlery dagger"]
    },
    "zombie":{
        "type":"Zombie",
        "health":3,
        "weapon_label":["fists","cutlery dagger","wooden spear","wooden sword"]
    },
    "vampire":{
        "type":"Vampire",
        "health":7,
        "weapon label":["wooden sword","wooden sword","cutlery dagger","ornate dagger"]
    },
    "ghost":{
        "type":"Ghost",
        "health":2,
        "weapon label":["fists","fists","cutlery dagger"]
    },
    "witch":{
        "type":"Witch",
        "health":3,
        "weapon label":["magic staff"]
    },
    "werewolf":{
        "type":"Werewolf",
        "health":6,
        "weapon label":["claws"]
    },
    "mother":{
        "type":"Mother",
        "health":4,
        "weapon label":["cane","slipper"]
    },
    "father":{
        "type":"Father",
        "health":5,
        "weapon label":["belt","taxes"]
    },
    "headless horseman":{
        "type":"Headless Horseman",
        "health":7,
        "weapon label":["horseman head","horseman head","horseman head","ornate dagger"]
    },
    "frankenstein monster": {
        "type":"Frankenstein's Monster",
        "health":14,
        "weapon label":["fists"]
    }
}

boss_data = {
    "type": "mega big scary monster",
    "health": 5,
    "weapon label": ["mega sword"]
}

def create_monster(label: str) -> Monster:
    data = monster_data[label]
    return Monster(data)

def create_random_monster() -> Monster:
    monster = random.choice(all_monsters())
    return create_monster(monster)

def create_boss() -> Monster:
    return Monster(boss_data)

def all_monsters():
    return list(monster_data.keys())

# Testing, do not delete.
if __name__ == "__main__":
    print(list(monster_data.keys()))
    entity = create_monster("ghost")
    print(entity.weapon.name)