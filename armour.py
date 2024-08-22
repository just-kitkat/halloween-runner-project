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
    "protection":20,
    "durability":None,
    "description":"This small tunic will protect you against the evil forces."
  },
  "chainmail":{
    "name":"Chainmail Tunic",
    "protection":30,
    "durability":None,
    "description":"A strong piece of armour, no doubt."
  },
  "iron":{
    "name":"Iron Breastplate",
    "protection":50,
    "durability":None,
    "description":"This massive piece of armour will protect you from the worst of hits..."
  },
  "":{
    "name":"Iron helmet",
    "protection":10,
    "durability":None,
    "description":"This head gear will serve you well"
  },
  "white tshirt":{
    "name":"White T-shirt",
    "protection":0,
    "durability":None,
    "description":"This fancy piece of fabric provides warmth from the cold, but no combat protection at all..."
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