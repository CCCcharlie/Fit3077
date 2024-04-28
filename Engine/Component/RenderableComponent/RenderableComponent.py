from pygame import Surface, Color
from pygame.locals import *
import pygame

from Engine import Entity 
from ..Component import Component
from Engine.Component.TransformComponent import TransformComponent

class RenderableComponent(Component):
  def __init__(self, owner: Entity):
    super().__init__(owner)
    self.showing: bool = True
    self.imageSurface: Surface = None
    self.colour = Color(255,255,255)

    self._generateImageSurface()

  def show(self):
    self.showing = True

  def hide(self):
    self.showing = False 

  def setColour(self, colour):
    self.colour = colour
    self._generateImageSurface()

  def getColour(self):
    return self.colour

  def _setImageSurface(self, imageSurface):
    self.imageSurface = imageSurface

  def _generateImageSurface(self):
    # create pink square  
    self.imageSurface = pygame.Surface((20,20))
    self.imageSurface.fill(Color(255,0,255))
    

  def render(self, display_surf: Surface):
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc is None:
      print("Component requires a tc to render")
      return
    
    if self.showing is False:
      return 
    
    display_surf.blit(self.imageSurface, (tc.x, tc.y))
