import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.RenderableComponent.RenderableComponent import RenderableComponent

class CircleComponent(RenderableComponent):
  def __init__(self, owner: Entity, radius: int):
    self.hidden = False
    self.radius = radius
    super().__init__(owner)

  def _generateImageSurface(self):
    image_surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
    image_surf = image_surf.convert()
    image_surf.fill((0,0,0,0))
    pygame.draw.circle(image_surf, self.getColour(), (self.radius, self.radius), self.radius)
    self._setImageSurface(image_surf)


