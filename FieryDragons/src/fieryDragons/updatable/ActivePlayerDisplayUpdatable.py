from typing import List
from engine.component.renderable.RenderableComponent import RenderableComponent
from engine.entity.Updateable import Updateable
from fieryDragons.Player import Player
from pygame import Color


class ActivePlayerDisplayUpdateable(Updateable):
  def __init__(self, playerColors: List[Color], renderable: RenderableComponent):
    self.__playerColors: List[Color] = playerColors
    self.__renderable: RenderableComponent = renderable


  def update(self, dt: float):
    self.__renderable.setColor(self.__playerColors[Player.ACTIVE_PLAYER.getPlayerNumber()])

  