from Engine import *

class ChitCard(Entity):
  def __init__(self, x, y):
    super().__init__()

    trans = TransformComponent(self,x,y)
    clickable = ClickableComponent(self,10,10)
    rect = RectComponent(self, 10,10,(255,255,255))

    self.add_component(trans)
    self.add_component(clickable)
    self.add_component(rect)