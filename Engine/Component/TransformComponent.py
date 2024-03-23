
from Engine import Entity
from .Component import Component


class TransformComponent(Component):
  def __init__(self, owner: Entity, x=0, y=0):
    super().__init__(owner)
    self.x = x
    self.y = y