
from enum import Enum

from engine.component.renderable.RenderableComponent import RenderableComponent
from fieryDragons.command.MoveActivePlayerCommand import MoveActivePlayerCommand
from fieryDragons.enums.AnimalType import AnimalType

class State(Enum):
  HIDDEN = 1
  VISIBLE = 2

class ChitCard:
  def __init__(self, front: RenderableComponent, back: RenderableComponent, animalType: AnimalType, amount: int):
    self.__front = front
    self.__back = back
    self.__state = State.HIDDEN
    self.__animalType: AnimalType = animalType
    self.__amount: int = amount

  def onClick(self):
    if self.__state == State.HIDDEN:
      self.state = State.VISIBLE
      self.__front.show()
      self.__back.hide()

      MoveActivePlayerCommand(self.__animalType, self.__amount).run()


  def onHide(self):
    self.state = State.HIDDEN
    self.__front.hide()
    self.__back.show()