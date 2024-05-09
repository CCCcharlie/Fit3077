from pygame import Surface, Color

from src.main.engine.component.renderableComponent.RenderableComponent import RenderableComponent
from src.main.engine.component.TransformComponent import TransformComponent


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

    self._setImageSurface(image_surf)
