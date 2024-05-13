
from __future__ import annotations

from typing import List
from engine.command.PrintCommand import PrintCommand
from engine.component.TransformComponent import TransformComponent
from fieryDragons.Segment import Segment
# from fieryDragons.TurnManager import TurnManager
from fieryDragons.enums.AnimalType import AnimalType


class Player:
  ACTIVE_PLAYER = None

  def __init__(self, startingSegment: Segment, transformComponent: TransformComponent, playerNumber: int):
    self.position: int = 0
    self.path: List[Segment] = startingSegment.generatePath(startingSegment)
    self.transformComponent = transformComponent

    self.__playerNumber: int = playerNumber
    self.__nextPlayer: Player = None 

    # snap to segment
    self._moveToSegment(startingSegment)

  def _moveToSegment(self, segment: Segment):
    self.transformComponent.position = segment.getSnapPosition()
    self.transformComponent.rotation = segment.getSnapRotation()

  def setNextPlayer(self, nextPlayer: Player):
     self.__nextPlayer = nextPlayer

  def traverse(self, caller: Player, start=False) -> List[Player]:
    if start:
     return self.__nextPlayer.traverse()

    if self == caller:
      return []
    return self.__nextPlayer.traverse(caller).append(self)
   
  def getPosition(self) -> Segment:
    return self.path[self.position]
  
  def _canMove(self, newSegment: Segment) -> bool:
    players = self.traverse(self, True)
    for player in players:
      if (player.getPosition() == self.position):
        return False
      return True

  def move(self, animalType: AnimalType, amount: int):

    if animalType is AnimalType.PIRATE_DRAGON:
      newLocation = self.position - amount
      newSegment = self.path[newLocation]
      if self._canMove(self, newSegment):
        self.position = newLocation
        self._moveToSegment(newSegment)

      # # end turn 
      Player.ACTIVE_PLAYER = self.__nextPlayer

    if animalType is self.path[self.position].getAnimalType():
      newLocation = self.position + amount

      #check if at the end of the path 
      if self.position >= len(self.path):
        #this player has won
        PrintCommand(f"Player {self.__playerNumber} wins!")

      newSegment = self.path[newLocation]

      #check can move there 
      if self._canMove(self, newSegment):
        self.position = newLocation
        self._moveToSegment(newSegment)
      else:
         Player.ACTIVE_PLAYER = self.__nextPlayer

    Player.ACTIVE_PLAYER = self.__nextPlayer



    

    
    
  

