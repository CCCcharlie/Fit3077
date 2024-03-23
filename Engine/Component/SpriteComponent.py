import Component
import pygame 
from pygame.locals import *

class SpriteComponent(Component):
  def __init__(self, owner, image=None):
    super().__init__(owner)

    if (image==None):

      # todo load in pink square ... 
      pass

    self.image = image

    self.image_surf = pygame.image.load("Game/Assets/" + self.image).convert()

  def render(self, display_surf):
    # get owner transform coords 
    display_surf.blit(self.image_surf, (0,0))
