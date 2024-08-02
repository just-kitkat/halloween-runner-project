class food:
  def __init__(self):
    self.healing = 0
    self.healing_per_turn = 0
    self.sanity = 0

  def use(self,player):
    #per turn the player takes how much he heals, its healing over time, decreases by 1 per turn until 0
    player.add_health(self.healing)
    player.add_healing_per_turn(self.healing_per_turn)
    player.gain_sanity(self.sanity)
    