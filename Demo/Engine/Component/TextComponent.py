import pygame 
from pygame.locals import *

from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent
from .Component import Component

class TextComponent(Component):
  def __init__(self, owner: Entity, text, font, colour):
    super().__init__(owner)

    self.text = text
    self.font = font
    self.colour = colour 

    self.text_surf = self.font.render(self.text, True, self.colour)

  def setText(self, text):
    self.text = text 

    self.text_surf = self.font.render(self.text, True, self.colour)

  def render(self, display_surf):
    # get owner transform coords 
    # ima be honest this code is terrible, lets use interfaces or something similar 
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc != None:
      #Add sprite to display coords
      display_surf.blit(self.text_surf, (tc.x, tc.y))
