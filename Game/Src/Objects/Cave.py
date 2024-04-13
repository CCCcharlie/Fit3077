from Engine import *

class Cave(Entity):
  def __init__(self):
    super().__init__()

    trans = TransformComponent(self,20,20)
    rect = RectComponent(self, 10,10,(255,255,255))

    self.add_component(trans)
    self.add_component(rect)