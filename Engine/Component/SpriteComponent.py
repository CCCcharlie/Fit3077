import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent
from .Component import Component

class SpriteComponent(Component):
  def __init__(self, owner: Entity, width, height, image=None,):
    super().__init__(owner)
    if (image==None):
      # todo load in pink square ... 
      pass

    self.image = image

    self.image_surf = pygame.image.load("Game/Assets/Sprites/" + self.image).convert()
    self.image_surf = pygame.transform.scale(self.image_surf, (width, height))

  def render(self, display_surf):
    # get owner transform coords 
    # ima be honest this code is terrible, lets use interfaces or something similar 
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc != None:
      #Add sprite to display coords
      display_surf.blit(self.image_surf, (tc.x, tc.y))
