import weapon
class monster:
  def __init__(self):
    self.health = 0
    self.weapon = weapon()

class skeleton(monster):
  def __init__(self)