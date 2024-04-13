import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent
from .Component import Component

class CircleComponent(Component):
  def __init__(self, owner: Entity, radius: int, colour):
    super().__init__(owner)
    self.hidden = False

    self.radius = radius
    self.image_surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
    self.image_surf = self.image_surf.convert()
    self.image_surf.fill((0,0,0,0))
    pygame.draw.circle(self.image_surf, colour, (radius, radius), radius)

  def hide(self):
    self.hidden = True

  def show(self):
    self.hidden = False

  def setColour(self, colour):
    self.image_surf.fill((0,0,0,0))
    pygame.draw.circle(self.image_surf, colour, (self.radius, self.radius), self.radius)

  def render(self, display_surf):
    if self.hidden:
      return

    # get owner transform coords 
    # ima be honest this code is terrible, lets use interfaces or something similar 
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc != None:
      #Add sprite to display coords
      display_surf.blit(self.image_surf, (tc.x - self.radius, tc.y - self.radius))
