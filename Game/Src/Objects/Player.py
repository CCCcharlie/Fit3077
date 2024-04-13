from Engine import *


class Player(Entity):
  def __init__(self, index):
    self.colours = [
      (255,102,204), #pink
      (0,255,0), # lime
      (255,255,0) # yellow
      (0,102,255) # blue
    ]
    self.index = 0
    self.colour = self.colours[self.index]


    trans = TransformComponent(self, 20,20)
    rect = RectComponent(self, 20, 20, self.colour)

    self.add_component(trans)
    self.add_component(rect)
