import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.RenderableComponent.RenderableComponent import RenderableComponent

class SpriteComponent(RenderableComponent):
  def __init__(self, owner: Entity, width, height, image=None):
    self.width = width
    self.height = height
    self.image = image
    super().__init__(owner)

  def _generateImageSurface(self):
    image_surf = pygame.image.load("Game/Assets/Sprites/" + self.image).convert()
    image_surf = pygame.transform.scale(image_surf, (self.width, self.height))

    self._setImageSurface(image_surf)
