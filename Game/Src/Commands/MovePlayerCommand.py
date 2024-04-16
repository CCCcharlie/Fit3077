from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Objects.TurnManager import TurnManager 

class MovePlayerCommand(Command):
  def __init__(self, player: Entity, moveDistance: int):
    self.player: Entity = player
    self.moveDistance: int = moveDistance


  def run(self):
    # get position of player
    initialPosition = TurnManager.CURRENT_POSITION
    moved = initialPosition.movePlayer(self.player, self.moveDistance)

    if moved:
      initialPosition.playerOnSquare = None
