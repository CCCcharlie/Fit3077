from engine.utils.Vec2 import Vec2
from pygame import Surface, Color, SRCALPHA, draw

from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent

class CircleComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, radius: int, color: Color, borderColor: Color = None):
    """
    Create a circle 
    Args:
      transformComponent (TransformComponent): The transform component the circle is attached to 
      width (int): The width of the circle
      height (int): The height of the circle
      color (Color): The color of the circle
      borderColor (Color): The color of the border (None for no border)
    """
    self.__radius: int = radius
    self.__borderColor: Color | None = borderColor
    self.__borderThickness: int = 2

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

  def setBorderThickness(self, borderThickness: int):
    """
    Set the border thickness
    
    Args:
      borderThickness (int): The thickness of the border to draw
    """
    self.__borderThickness = borderThickness
  
  def _generateImageSurface(self) -> None:
    """
    Generate a circle on an image surface
    """
    image_surf = Surface((self.__radius * 2, self.__radius * 2), SRCALPHA)
    draw.circle(image_surf, self._color, (self.__radius, self.__radius), self.__radius)
    if self.__borderColor is not None:
      draw.circle(image_surf, self.__borderColor,(self.__radius, self.__radius), self.__radius, self.__borderThickness)

    self._setImageSurface(image_surf)
