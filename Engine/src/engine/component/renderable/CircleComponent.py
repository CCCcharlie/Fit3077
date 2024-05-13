from engine.utils.Vec2 import Vec2
from pygame import Surface, Color, SRCALPHA, draw

from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent

class CircleComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, radius: int, color: Color):
    """
    Create a circle 
    Args:
      transformComponent (TransformComponent): The transform component the circle is attached to 
      width (int): The width of the circle
      height (int): The height of the circle
      color (Color): The color of the circle
    """
    self.__radius: int = radius
    super().__init__(transformComponent)
    self.setColor(color)


  def _pivot(self) -> Vec2:
    return Vec2(self.__radius, self.__radius)

  def setRadius(self, radius: int) -> None:
    """
    Set the circles radius
    """
    self.__radius = radius
    self._generateImageSurface()
  
  def _generateImageSurface(self) -> None:
    """
    Generate a circle on an image surface
    """
    image_surf = Surface((self.__radius * 2, self.__radius * 2), SRCALPHA)
    draw.circle(image_surf, self._color, (self.__radius, self.__radius), self.__radius)
    self._setImageSurface(image_surf)
