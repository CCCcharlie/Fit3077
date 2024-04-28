import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.RenderableComponent.RenderableComponent import RenderableComponent


class TextComponent(RenderableComponent):
  def __init__(self, owner: Entity, text: str, font: pygame.font.Font):
    self.text: str = text
    self.font = font
    super().__init__(owner)

  def setText(self, text: str):
    self.text = text 
    self._generateImageSurface()

  def setFont(self, font):
    self.font = font
    self._generateImageSurface()

  def _generateImageSurface(self):
    text_surf = self.font.render(self.text, True, self.getColour())
    self._setImageSurface(text_surf)


