from pygame import Surface, Color

from main.engine.component.RenderableComponent.RenderableComponent import RenderableComponent
from main.engine.component.TransformComponent import TransformComponent


class RectComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, width: int, height: int, colour: Color):
    """
    Create a rectangle
    """
    self.__width: int = width
    self.__height: int = height
    self.__colour: Color = colour
    super().__init__(transformComponent)

  def setColour(self, colour: Color) -> None:
    """
    Set the rectangle colour
    """
    self.__colour = colour
  
  def _generateImageSurface(self) -> None:
    """
    Generate a rectangle on an image surface
    """
    image_surf = Surface((self.__width, self.__height))
    image_surf = image_surf.convert()
    image_surf.fill(self.__colour)
