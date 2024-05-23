from __future__ import annotations

from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from engine.builder.SceneBuilder import SceneBuilder
from fieryDragons.save.SaveManager import SaveManager
from pygame import Color


class PlayerBuilder:
  playerColors = [
      Color(44,173,199),
      Color(214,2,87),
      Color(199,184,20),
      Color(53,199,20)
    ]
  
  def __init__(self):
    self.__playerNumber = 0

    self.__startingSegment: Segment = None
    self.__startingSegmentChanged = False


    self.__firstPlayer: Player = None
    self.__previousPlayer: Player = None


  def setStartingSegment(self, startingSegment: Segment) -> PlayerBuilder:
    self.__startingSegment = startingSegment
    self.__startingSegmentChanged = True
    return self

  def finish(self):
    self.__previousPlayer.setNextPlayer(self.__firstPlayer)
    Player.ACTIVE_PLAYER = self.__firstPlayer

  def build(self) -> Entity:
    #error handling
    if self.__startingSegmentChanged is False:
      return IncompleteBuilderError(self.__class__.__name__, "Starting Segment Unchanged")

    self.__startingSegmentChanged = False

    t = TransformComponent()
    p = Player(self.__startingSegment, t, self.__playerNumber)
    SaveManager().register(p)
    
    if (self.__playerNumber == 0):
      self.__firstPlayer = p
    else:
      self.__previousPlayer.setNextPlayer(p)
    self.__previousPlayer = p
    
    r = RectComponent(t, 50,50,PlayerBuilder.playerColors[self.__playerNumber])
    self.__playerNumber += 1


    e = Entity()
    e.add_renderable(r)
    return e


   


    