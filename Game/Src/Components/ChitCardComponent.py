from Engine import Component, Entity, CircleComponent
from enum import Enum

from Engine.Component.CommandComponent import CommandComponent
from Game.Src.Commands.MovePlayerCommand import MovePlayerCommand
from Game.Src.Objects.TurnManager import TurnManager

class State(Enum):
  HIDDEN = 1
  VISIBLE = 2

class ChitCardComponent(Component):
  def __init__(self, owner: Entity, front: CircleComponent, back: CircleComponent):
    super().__init__(owner)
    self.front = front
    self.back = back
    self.state = State.HIDDEN

    self.front.hide()

  def onClick(self):
    if self.state == State.HIDDEN:
      self.state = State.VISIBLE
      self.front.show()
      self.back.hide()

      #create and run the command
      cc: CommandComponent = self.owner.get_component(CommandComponent)
      if cc != None:
        cc.addCommand(MovePlayerCommand(TurnManager.PLAYER, 1))