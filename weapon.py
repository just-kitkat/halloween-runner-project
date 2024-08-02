import random
class weapon:
  def __init__(self,name):
    self.damage = 0
    self.durability = 0
    self.defense = 0
    self.name = name
    #accuracy is a integer from 1-100, acts as percentage chance of missing
    self.accuracy = 1
  #generalised for both enemies and the player
  def attack(self,entity):
    if random.randint(1,100)>self.accuracy:
      #attack missed
      return False
    else:
      #attack hit
      entity.reduce_health()
      return True