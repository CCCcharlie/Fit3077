from __future__ import annotations

from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from fieryDragons.save.SaveManager import SaveManager
from fieryDragons.VolcanoCard import VolcanoCard

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

    self.__startingVolcanoCard: VolcanoCard = None

    self.__firstPlayer: Player = None
    self.__previousPlayer: Player = None

    self.__animate = True

  def setStartingVolcanoCard(self, startingVolcanoCard: VolcanoCard) -> PlayerBuilder:
    self.__startingVolcanoCard = startingVolcanoCard
    return self

  def setAnimate(self, value : bool) -> PlayerBuilder:
      self.__animate = value
      return self

  def finish(self):
    self.__previousPlayer.setNextPlayer(self.__firstPlayer)
    Player.ACTIVE_PLAYER = self.__firstPlayer

  def build(self) -> Entity:
    # first generate path
    path = self.__startingVolcanoCard.generatePath()

    t = TransformComponent()
    p = Player(path, t, self.__playerNumber)

    if self.__animate:
        #slowly move player to segment from middle
        start = TransformComponent()
        start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
        playerDelayMove = DelayExecuteMFMFCommand(
          LinearMoveMFCommand(
            start,
            path[0].getSnapTransform(),
            t, 
            500
          ),
          4500
        )
        MultiFrameCommandRunner().addCommand(playerDelayMove)
        playerDelayMove.run()
        t.position = Vec2(-100,-100)
    else:
        t.position = path[0].getSnapTransform().position

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
