from Engine import *

class ChitCard(Entity):
  def __init__(self, x, y, radius):
    super().__init__()

    trans = TransformComponent(self,x,y)
    clickable = ClickableComponent(self,10,10)
    circ = CircleComponent(self, radius, (161,156,14))

    self.add_component(trans)
    self.add_component(clickable)
    self.add_component(circ)