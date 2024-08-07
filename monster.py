import random
import math
from weapon import Fists

class Monster:
    def __init__(self):
        #name can be seperate from monster type
        spooky_names = ["Morticia", "Vlad", "Lilith", "Raven", "Draven", "Seraphina", "Elvira", "Damien", "Hecate", "Bram"]
        spooky_surnames = ["Blackwood", "Nightshade", "Graves", "Vesper", "Thorn", "Shadow", "Bloodworth", "Moonfall", "Darkmore", "Grimwood"]
        self.name = spooky_names[random.randint(0,len(spooky_names)-1)]+" "+ spooky_surnames[random.randint(0,len(spooky_surnames)-1)]

        #fists is the basic weapon assigned to each enemy, child class of weapon
        self.weapon = Fists()
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


class Skeleton(Monster):
    def __init__(self,multiplier,name):
        #subject to change
        self.health = math.ceil(random.randint(1,5)*multiplier)
        #ranged is a child class of parent weapon
        self.weapon = ranged(name)