import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent
from .Component import Component

class RectComponent(Component):
  def __init__(self, owner: Entity, width: int, height: int, colour):
    super().__init__(owner)

    self.width = width
    self.height = height
    self.colour = colour
    self.image_surf = pygame.Surface((self.width, self.height))
    self.image_surf = self.image_surf.convert()
    self.image_surf.fill(colour)

  def render(self, display_surf):
    # get owner transform coords 
    # ima be honest this code is terrible, lets use interfaces or something similar 
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc != None:
      #Add sprite to display coords
      display_surf.blit(self.image_surf, (tc.x, tc.y))
