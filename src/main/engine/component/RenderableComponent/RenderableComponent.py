from abc import ABC, abstractmethod

import pygame
from main.engine.Renderable import Renderable
from pygame import Surface

from main.engine.component.TransformComponent import TransformComponent
from main.engine.utils.Vec2 import Vec2

class RenderableComponent(ABC, Renderable):
  """
  Renderable component for use with common renderables including squares, circles etc
  give it an image surface and it will handle rendering to a specific position
  """
  def __init__(self, transformComponent: TransformComponent):
    """
    Create a new renderable component.

    Calls protected _generateImageSurface upon any change 
    Provides _setImageSurface for use by child 
    """
    self.__showing: bool = True
    self.__imageSurface: Surface = None
    self.__transformComponent: TransformComponent = transformComponent

    self._generateImageSurface()


  @abstractmethod
  def _generateImageSurface(self) -> None:
    """
    Generate the image surface.
    """

  def _setImageSurface(self, imageSurface: Surface) -> None:
    """
    Set the renderable components image surface.
    """
    self.__imageSurface = imageSurface

  def show(self) -> None:
    """
    Show the renderable component.
    """
    self.__showing = True

  def hide(self) -> None:
    """
    Hide the renderable component.
    """
    self.__showing = False 

  def render(self, display_surf: Surface) -> None:
    """
    Render the renderable component.
    """
    if self.__showing is False:
      return 
    
    image: Surface = self.__imageSurface
    
    #Scale surface based on scale information
    scale: Vec2 = self.__transformComponent.scale
    image = pygame.transform.scale(image, scale.toTuple())

    #Rotate based on rotation information
    rotation: int = self.__transformComponent.rotation
    image = pygame.transform.rotate(image, rotation)
    
    #blit to screen
    position: Vec2 = self.__transformComponent.position
    display_surf.blit(self.__imageSurface, position.toTuple())
