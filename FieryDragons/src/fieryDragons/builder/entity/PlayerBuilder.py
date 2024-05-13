from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from pygame import Color


class PlayerBuilder:
  def __init__(self):
    self.__playerNumber = 0

    self.__startingSegment: Segment = None
    self.__startingSegmentChanged = False


    self.__firstPlayer: Player = None
    self.__previousPlayer: Player = None


  def setStartingSegment(self, startingSegment: Segment):
    self.__startingSegment = startingSegment
    self.__startingSegmentChanged = True

  def finish(self):
    self.__previousPlayer.setNextPlayer(self.__firstPlayer)

  def build(self) -> Entity:
    #error handling
    if self.__startingSegmentChanged is False:
      return IncompleteBuilderError(self.__class__.__name__, "Starting Segment Unchanged")

    self.__startingSegmentChanged = False

    t = TransformComponent()
    p = Player(self.__startingSegment, t, self.__playerNumber)

    if (self.__playerNumber == 0):
      self.__firstPlayer = p
    else:
      self.__previousPlayer.setNextPlayer(p)
      self.__previousPlayer = p
    
    r = RectComponent(t, 50,50,Color(255,0,0))
    self.__playerNumber += 1


    e = Entity()
    e.add_renderable(r)
    return e


   


    