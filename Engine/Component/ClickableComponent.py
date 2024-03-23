
from Engine import Entity
from .Component import Component
from Engine.Input import Input
from Engine.Component.TransformComponent import TransformComponent


class ClickableComponent(Component):
  def __init__(self, owner: Entity, width: int, height: int):
    self.owner = owner
    self.width = width
    self.height = height


    self.inside = False
    self.clicked = False

  def update(self):
    # get owner transform coords 
    # ima be honest this code is terrible, lets use interfaces or something similar 
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc ==None:
      tc = {}
      tc['x'] = 0
      tc['y'] = 0

    # x range is tc.x -> tc.x + self.width
    # y range is tx.y -> tc.y + self.height
    mx, my = Input.getmouseposition()

    self.inside = tc.x <= mx <= tc.x + self.width and tc.y <= my <= tc.y + self.height

    if (self.inside):
      self.clicked = Input.getMouseButton(1)



