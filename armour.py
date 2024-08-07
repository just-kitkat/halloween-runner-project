import math
class armour:
  def __init__(self):
    self.name = "Noname"
    self.protection = 0
    self.durability = 0

  def get_protection(self):
    return self.protection

  def get_durability(self):
    return self.durability

  def lose_durability(self,multi):
    self.durability -= math.ceil(1*multi)

"""
Class helmet
reduces crit chance
Class chestplate
dmg reduction
Class leggings
dmg reduction
Class boots
more number of moves, "agility"
"""