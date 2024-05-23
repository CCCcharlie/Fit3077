from __future__ import annotations

from typing import List
from engine.entity.Renderable import Renderable
from engine.entity.Updateable import Updateable
from pygame.font import SysFont
from pygame import Color

from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.entity.Entity import Entity
from engine.utils.Vec2 import Vec2
from fieryDragons.updatable.ActivePlayerDisplayUpdatable import ActivePlayerDisplayUpdateable



class ActivePlayerDisplayBuilder:
  def __init__(self):
    self.__playerColors: List[Color] = [] 
    self.__position: Vec2 = Vec2(10,10)

  def setPlayerColors(self, playerColors: List[Color]) -> ActivePlayerDisplayBuilder:
    self.__playerColors = playerColors
    return self
  
  def setPosition(self, position: Vec2) -> ActivePlayerDisplayBuilder:
    self.__position = position
    return self

  def build(self) -> Entity:
    e = Entity()

    t = TransformComponent()
    t.position = self.__position

    rect: Renderable = RectComponent(t, 180, 30, Color(0,0,0))
    text: Renderable = TextComponent(t, "Active Player", SysFont("Corbel", 30), Color(0,0,0))
    apu: Updateable = ActivePlayerDisplayUpdateable(self.__playerColors, rect)

    e.add_renderable(rect)
    e.add_renderable(text)
    e.add_updateable(apu)

    return e
