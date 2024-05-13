from abc import abstractmethod
from typing import Tuple

import pygame
from pygame import Surface, Color, Rect
from ...entity.Renderable import Renderable
from ...component.TransformComponent import TransformComponent
from ...utils.Vec2 import Vec2

class RenderableComponent(Renderable):
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
    self._color: Color = Color(255,255,255)

    self._generateImageSurface()

  def setColor(self, color: Color):
    """
    Set the renderables colour
    """
    self._color = color
    self._generateImageSurface()

  @abstractmethod
  def _generateImageSurface(self) -> None:
    """
    Generate the image surface.
    """
    raise NotImplementedError()

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

  def _pivot(self) -> Vec2:
    return Vec2(0,0)
  

  def __rotate(self, image: Surface) -> Tuple[Surface, Rect]:
    """
    rotate surface
    """
    rotation: int = self.__transformComponent.rotation
    pivot: Vec2 = self._pivot()

    rotatedImage = pygame.transform.rotate(image, rotation)
    rotatedPivot = pygame.Vector2(pivot.x, pivot.y).rotate(rotation)
    rect = rotatedImage.get_rect(center=rotatedPivot)    
    return (rotatedImage, rect)

  def render(self, display_surf: Surface) -> None:
    """
    Render the renderable component.
    """
    if self.__showing is False:
      return 
    
    image: Surface = self.__imageSurface

    #Scale surface based on scale information
    # scale: Vec2 = self.__transformComponent.scale
    # image = pygame.transform.scale(image, scale.toTuple())

    # #Rotate
    # image, rect = self.__rotate(image)

    # apply position
    rect = image.get_rect()
    position: Vec2 = self.__transformComponent.position
    rect.x += position.x
    rect.y += position.y

    # apply offset
    offset = self._pivot()
    rect.x += offset.x
    rect.y += offset.y

    #blit to screen
    display_surf.blit(image, rect)

    
    pygame.draw.circle(display_surf, Color(0,0,0), position.toTuple(), 2)

