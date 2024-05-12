
from enum import Enum

from Engine.src.engine.component.renderable.RenderableComponent import RenderableComponent

class State(Enum):
  HIDDEN = 1
  VISIBLE = 2

class ChitCardComponent:
  def __init__(self, front: RenderableComponent, back: RenderableComponent):
    self.__front = front
    self.__back = back
    self.__state = State.HIDDEN

  def onClick(self):
    if self.__state == State.HIDDEN:
      self.state = State.VISIBLE
      self.__front.show()
      self.__back.hide()

      ## run the move player command here

  def onHide(self):
    self.state = State.HIDDEN
    self.__front.hide()
    self.__back.show()