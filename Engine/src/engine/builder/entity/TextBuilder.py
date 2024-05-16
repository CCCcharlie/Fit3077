from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.entity.Entity import Entity
from engine.utils.Vec2 import Vec2
from pygame import Color
from pygame.font import Font, SysFont


class TextBuilder:
  def __init__(self):
    self.__pos: Vec2 = Vec2(10,10)
    self.__text: str = "Empty String"
    self.__textColor: Color = Color(255,255,255)
    self.__rectWidth: int = 500
    self.__rectHeight: int = 60
    self.__rectColor: Color = Color(0,0,0)
    self.__font: Font = SysFont("Corbel", 60)

  def setPosition(self, pos: Vec2) -> TextBuilder:
    self.__pos = pos
    return self

  def setText(self, text: str) -> TextBuilder:
    self.__text = text
    return self

  def setTextColor(self, textColor: Color) -> TextBuilder:
    self.__textColor = textColor
    return self
  
  def setRectWidth(self, width: int) -> TextBuilder:
    self.__rectWidth = width
    return self
  
  def setRectHeight(self, height: int) -> TextBuilder:
    self.__rectHeight = height
    return self
  
  def setRectColor(self, color: Color) -> TextBuilder:
    self.__textColor = color
    return self
  
  def setFont(self, font: Font) -> TextBuilder:
    self.__font = font
    return self

  def build(self,) -> Entity:
    e = Entity()
    
    transformComponent = TransformComponent()
    self.__transformComponent = transformComponent
    transformComponent.position = self.__pos
    rect = RectComponent(transformComponent, self.__rectWidth, self.__rectHeight, self.__rectColor)
    textComponent = TextComponent(transformComponent, self.__text, self.__font, self.__textColor)

    e.add_renderable(rect)
    e.add_renderable(textComponent)
    return e
