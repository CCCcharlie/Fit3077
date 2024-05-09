from pygame import Surface, Color, SRCALPHA, draw

from main.engine.component.RenderableComponent.RenderableComponent import RenderableComponent
from main.engine.component.TransformComponent import TransformComponent

class CircleComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, radius: int, colour: Color):
    """
    Create a circle 
    """
    self.__radius: int = radius
    self.__colour: Color = colour
    super().__init__(transformComponent)

  def setColour(self, colour: Color) -> None:
    """
    Set the images colour
    """
    self.__colour = colour

  def setRadius(self, radius: int) -> None:
    """
    Set the circles radius
    """
    self.__radius = radius
  
  def _generateImageSurface(self) -> None:
    """
    Generate a circle on an image surface
    """
    image_surf = Surface((self.__radius * 2, self.__radius * 2), SRCALPHA)
    draw.circle(image_surf, self.__colour, (self.__radius, self.__radius), self.__radius)
    self._setImageSurface(image_surf)