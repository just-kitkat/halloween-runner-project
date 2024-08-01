import random
class weapon:
  def __init__(self,name):
    self.damage = 0
    self.durability = 0
    self.defense = 0
    self.name = name
    #accuracy is a integer from 1-100, acts as percentage chance of missing
    self.accuracy = 1

  def attack(self,monster):
    if random.randint(1,100)>self.accuracy:
      print("(Placeholder) attack missed!")
    else:
      print("(Placeholder) monster took damage!")
      monster.health -= self.damage

  def block(self,monster,player):
    if random.randint(1,100)<monster.weapon.accuracy:
      pass
    else:
      player.health -= monster.damage