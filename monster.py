import random
import math
from weapon import Weapon,create_weapon,all_weapons
class Monster:
    def __init__(self,data):
        self.name = name()
        #fists is the basic weapon assigned to each enemy, child class of weapon
        self.weapon = create_weapon("Fists")
        self.health = 0

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

def create_monster(label: str) -> Monster:
    data = monster_data[label]
    return Weapon(data)