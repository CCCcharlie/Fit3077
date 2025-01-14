
from __future__ import annotations

from typing import Dict, List
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.DelayExecuteMFCommand import DelayExecuteMFCommand
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.command.ShakeMFCommand import ShakeMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.Segment import Segment
from fieryDragons.builder.scene.WinSceneBuilder import WinSceneBuilder

from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from engine.Serializable import Serializable


class Player(Serializable):
  ACTIVE_PLAYER: Player = None

  def __init__(self, path: List[Segment], transformComponent: TransformComponent, playerNumber: int):
    self.position: int = 0
    self.path: List[Segment] = path
    self.transformComponent = transformComponent

    self.__playerNumber: int = playerNumber
    self.__nextPlayer: Player = None 
    super().__init__()

    # snap to segment
    #self._moveToSegment(startingSegment)

  def getPlayerNumber(self)-> int:
    return self.__playerNumber
  
  def getDistanceToPlayer(self, player: Player):
    """
    Gets the distance to the other player 

    returns none if the player is not on this players path 

    Args:
      player (Player): the other player to check the distance to 
    """
    otherSegment: Segment = player.getPosition()

    distance = None

    segmentIndex = 0
    try:
      segmentIndex = self.path.index(otherSegment)
    except ValueError:
        return None
    
    # if i am in cave also skip
    if self.position == 0:
      return None
    
    
    # convert segment index into distance 
    # accounting for the fact that it is a circle, 
    # ignoring the first and last element as they are caves
    
    # this ignores the first index in the list as cave
    adjustedSelfPosition = self.position - 1
    adjustedOtherPosition = segmentIndex - 1
    adjustedCircleLength = len(self.path) - 2 # this ignores the last index as it is a cave 

    # now calculate distance from this adjusted position.

    distance = segmentIndex - self.position

    if adjustedOtherPosition >= adjustedSelfPosition:
        distance = adjustedOtherPosition - adjustedSelfPosition
    else:
        distance = adjustedCircleLength - adjustedSelfPosition + adjustedOtherPosition

    return distance


  def _moveToSegment(self, segment: Segment):
    command = LinearMoveMFCommand(self.transformComponent.clone(), segment.getSnapTransform(), self.transformComponent, 500)
    MultiFrameCommandRunner().addCommand(command)
    command.run()

  def setNextPlayer(self, nextPlayer: Player):
     self.__nextPlayer = nextPlayer

  def traverse(self, caller: Player, start=False) -> List[Player]:
    if start:
      return self.__nextPlayer.traverse(caller, False)
     
    if self == caller:
      return []

    lst: List[Player] = self.__nextPlayer.traverse(caller, False)
    lst.append(self)
    return lst
   
  def getPosition(self) -> Segment:
    return self.path[self.position]
  
  def __canMove(self, newSegment: Segment) -> bool:
    players = self.traverse(self, True)
    for player in players:
      if (player.getPosition() == newSegment):
        return False
    return True
    
  def endTurn(self):
    # shake self

    Player.ACTIVE_PLAYER = self.__nextPlayer
    #print(f"Active player is {self.__nextPlayer.__playerNumber}")
    PlayerTurnEndEmitter().notify()

  def forceMoveToSegment(self, segment: Segment):
    """
    Moves a player to a segment, overrides checks 
    """
    self._moveToSegment(segment)
    self.position = self.path.index(segment)

  def move(self, animalType: AnimalType, amount: int):
    # CASE picked pirate dragon
    if animalType is AnimalType.PIRATE_DRAGON:
      newLocation = self.position - amount
      newLocation = max(0,newLocation) # prevent the play from moving too far back
      newSegment = self.path[newLocation]
      if self.__canMove(newSegment):
        self.position = newLocation
        self._moveToSegment(newSegment)
      self.endTurn()
      return
  
    #CASE picked the right animal
    if animalType is self.path[self.position].getAnimalType():
      newLocation = self.position + amount

      #CASE at end of path
      if newLocation >= len(self.path) - 1:
        #this player has won
        newLocation = len(self.path) - 1
        self._moveToSegment(self.path[newLocation])

        winSceneBuilder = WinSceneBuilder().setWinningPlayer(str(self.__playerNumber))
        csc = ChangeSceneCommand(winSceneBuilder)
        command = DelayExecuteMFCommand(csc, 1000)
        MultiFrameCommandRunner().addCommand(command)
        command.run()
        return

      newSegment = self.path[newLocation]

      
      if self.__canMove(newSegment):
        #CASE CAN MOVE 
        self.position = newLocation
        self._moveToSegment(newSegment)
        return
      else:
        # CASE CANT MOVE
        command = ShakeMFCommand(5, self.transformComponent, 500)
        MultiFrameCommandRunner().addCommand(command)
        command.run()
        self.endTurn()
        return

    # CASE picked the wrong animal
    command = ShakeMFCommand(5, self.transformComponent, 500)
    MultiFrameCommandRunner().addCommand(command)
    command.run()
    self.endTurn()
    return
  
  def serialise(self) -> Dict:
    d: dict = {}
    d["location"] = self.position
    d["active"] = Player.ACTIVE_PLAYER == self
    return d
  
  def deserialise(self, data: Dict) -> None:
    location = data["location"]
    self.position = int(location)

    #slowly move player from cave to current position
    playerDelayMove = DelayExecuteMFMFCommand(
      LinearMoveMFCommand(
        self.path[0].getSnapTransform(),
        self.getPosition().getSnapTransform(),
        self.transformComponent,
        500
      ),
      5000
    )
    MultiFrameCommandRunner().addCommand(playerDelayMove)
    playerDelayMove.run()

    active = data["active"]
    if active:
      Player.ACTIVE_PLAYER = self
    return



    

    
    
  

