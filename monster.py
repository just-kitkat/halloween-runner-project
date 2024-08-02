import random
import math
class monster:
  def __init__(self,name):
    #name can be seperate from monster type
    self.name = name
    self.health = 0
    #fists is the basic weapon assigned to each enemy, child class of weapon
    self.weapon = fists()
    #damage is done inside weapon class
  def attack(self,entity):
    bool = self.weapon.attack(entity)
    if bool:
      print(f"{self.name}\'s attack hit,[ {self.weapon.damage}] damage dealt")
    else:
      print(f"{self.name}\'s attack missed!")
      

  def block(self,entity):
    bool = entity.attack(self)
    if bool:
      print(f"{self.name}\'s attack hit,[ {self.weapon.damage}] damage dealt")
    else:
      print(f"{self.name}\'s attack missed!")


class skeleton(monster):
  def __init__(self,multiplier,name):
    #subject to change
    self.health = math.ceil(random.randint(1,5)*multiplier)
    #ranged is a child class of parent weapon
    self.weapon = ranged(name)