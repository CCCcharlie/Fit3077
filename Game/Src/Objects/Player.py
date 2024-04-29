from Engine import *


class Player(Entity):
  def __init__(self, index=0):
    super().__init__()
    self.colours = [
      (0,0,0), #pink
      (255,165,0), # lime
      (255,255,0), # yellow
      (0,102,255) # blue
    ]
    self.index = index
    self.colour = self.colours[self.index]


    trans = TransformComponent(self, -100,-100) # spawn this guy off the screen
    rect = RectComponent(self, 10, 10)
    rect.setColour(self.colour)

    self.add_component(trans)
    self.add_component(rect)
