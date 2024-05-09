from pygame import image, transform

from src.main.engine.component.renderableComponent.RenderableComponent import RenderableComponent
from src.main.engine.component.TransformComponent import TransformComponent



class SpriteComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, width: float, height: float, image: str=None) -> None:
    """
    Create a sprite

    Args:
      width (float): The scaling factor for the sprites width
      height (float): The scaling factor for the sprites height
      image (str): The path to the sprite in the sprites folder
    """
    self.__width: float = width
    self.__height: float = height
    self.__image: str = image
    super().__init__(transformComponent)

  def _generateImageSurface(self):
    image_surf = image.load("asset/sprite/" + self.__image).convert()
    image_surf = transform.scale(image_surf, (self.__width, self.__height))

    self._setImageSurface(image_surf)
