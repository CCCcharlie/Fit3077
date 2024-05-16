
from __future__ import annotations

from typing import List
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.command.PrintCommand import PrintCommand
from engine.command.ShakeMFCommand import ShakeMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from fieryDragons.Segment import Segment
# from fieryDragons.TurnManager import TurnManager
from fieryDragons.builder.scene.SceneBuilder import SceneBuilder
from fieryDragons.builder.scene.WinSceneBuilder import WinSceneBuilder

from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from pygame import Color


class Player:
  ACTIVE_PLAYER: Player = None
  RESET_SCENE_BUILDER: SceneBuilder = None

  def __init__(self, startingSegment: Segment, transformComponent: TransformComponent, playerNumber: int):
    self.position: int = 0
    self.path: List[Segment] = startingSegment.generatePath(startingSegment)
    self.transformComponent = transformComponent

    self.__playerNumber: int = playerNumber
    self.__nextPlayer: Player = None 

    # snap to segment
    self._moveToSegment(startingSegment)

  def getPlayerNumber(self)-> int:
    return self.__playerNumber

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
        winScene = WinSceneBuilder().setResetScene(Player.RESET_SCENE_BUILDER).setWinningPlayer(str(self.__playerNumber)).build()
        ChangeSceneCommand(winScene).run()
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



    

    
    
  

