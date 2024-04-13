from Engine import Component, Entity, CircleComponent
from enum import Enum

class State(Enum):
  HIDDEN = 1
  VISIBLE = 2

class ChitCardComponent(Component):
  def __init__(self, owner: Entity, front: CircleComponent, back: CircleComponent):
    self.owner = owner
    self.front = front
    self.back = back
    self.state = State.HIDDEN

    self.front.hide()

  def onClick(self):
    if self.state == State.HIDDEN:
      self.state = State.VISIBLE
      self.front.show()
      self.back.hide()