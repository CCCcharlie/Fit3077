from Engine import *


class Player(Entity):
  def __init__(self, index=0):
    super().__init__()
    self.colours = [
      (255,102,204), #pink
      (0,255,0), # lime
      (255,255,0), # yellow
      (0,102,255) # blue
    ]
    self.index = index
    self.colour = self.colours[self.index]


    trans = TransformComponent(self, -100,-100) # spawn this guy off the screen
    rect = RectComponent(self, 20, 20, self.colour)

    self.add_component(trans)
    self.add_component(rect)
