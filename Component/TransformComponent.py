import Component

class TransformComponent(Component):
  def __init__(self, owner, x=0, y=0):
    super().__init__(owner)
    self.x = x
    self.y = y