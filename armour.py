import math
import random

class Armour:
  def __init__(self,data):
    self.name = data["name"]
    self.protection = data["protection"]
    self.durability = data["durability"]
    self.description = data["description"]

armour_data = {
  "leather":{
    "name":"Leather Tunic",
    "protection":10,
    "durability":None,
    "description":"[placeholder]"
  },
  "chainmail":{
    "name":"Chainmail Tunic",
    "protection":20,
    "durability":None,
    "description":"[placeholder]"
  },
  "iron":{
    "name":"Iron Breastplate",
    "protection":30,
    "durability":None,
    "description":"[placeholder]"
  },
  "white tshirt":{
    "name":"White T-shirt",
    "protection":0,
    "durability":None,
    "description":"[placeholder]"
  },
}

def create_armour(label: str) -> Armour:
  data = armour_data[label]
  return Armour(data)

def create_random_armour() -> Armour:
  armour = random.choice(all_armour())
  return create_armour(armour)

def all_armour():
  return list(armour_data.keys())

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