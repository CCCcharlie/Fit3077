import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.RenderableComponent.RenderableComponent import RenderableComponent

class RectComponent(RenderableComponent):
  def __init__(self, owner: Entity, width: int, height: int):
  
    self.width = width
    self.height = height

    super().__init__(owner)


  def _generateImageSurface(self):
    image_surf = pygame.Surface((self.width, self.height))
    image_surf = image_surf.convert()
    image_surf.fill(self.getColour())

    self._setImageSurface(image_surf)


  
    
    
    
  