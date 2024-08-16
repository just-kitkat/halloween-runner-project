import random
from player import add_health

class Food:
  def __init__(self,data):
    self.name = data["name"]
    self.healing = data["health"]

  def use(self,player):
    #per turn the player takes how much he heals, its healing over time, decreases by 1 per turn until 0
    player.add_health(self.healing)

food_data = {
  "apple":{
    "name":"Apple",
    "health":3
  },
  "orange":{
    "name":"Orange",
    "health":3
  },
  "durian":{
    "name":"Mao Shan Wang Durian",
    "health":9
  },
  "chocolate":{
    "name":"Ferrero Rocher",
    "health":6
  },
  "mala":{
    "name":"Mala",
    "health":3
  },
}
def create_food(label: str) -> Food:
  data = food_data[label]
  return Food(data)

def create_random_food() -> Food:
  food = random.choice(all_food())
  return create_food(food)

def all_food():
  return list(food_data.keys())