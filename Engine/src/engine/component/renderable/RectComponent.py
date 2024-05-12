from pygame import Surface, Color

from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent


class RectComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, width: int, height: int, color: Color):
    """
    Create a rectangle

    Args:
      transformComponent (TransformComponent): The transform component the rectangle is attached to 
      width (int): The width of the rectangle
      height (int): The height of the rectangle
      color (Color): The color of the rectangle
    """
    self.__width: int = width
    self.__height: int = height
    super().__init__(transformComponent)
    self.setColor(color)

  
  def _generateImageSurface(self) -> None:
    """
    Generate a rectangle on an image surface
    """
    image_surf = Surface((self.__width, self.__height))
    image_surf = image_surf.convert()
    image_surf.fill(self._color)

    self._setImageSurface(image_surf)
