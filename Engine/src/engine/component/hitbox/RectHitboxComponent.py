from pygame import Surface, Rect, draw
from engine.utils.Vec2 import Vec2
from engine.component.TransformComponent import TransformComponent
from engine.component.hitboxComponent.HitboxComponent import HitboxComponent


class RectHitboxComponent(HitboxComponent):
  """
  Rectangle hitbox component
  
  For now the scaling and rotation doesn't work
  """
  def __init__(self, transformComponent: TransformComponent, width: int, height: int, debug=False):
    """
    Create the hitbox
    
    Args:
      transformComponent (TransformComponent): The transform this hitbox is attached to
      width (int): The width of the hitbox
      height (int): The height of the hitbox
      debug (bool): If True will render the hitbox shape
    """
    super().__init__(transformComponent, debug)
    self.__width = width
    self.__height = height

  @property
  def width(self) -> int:
    return self.__width
  
  @width.setter
  def width(self, value):
    self.__width = value

  @property
  def height(self) -> int:
    return self.__height
  
  @height.setter
  def height(self, value: int):
    self.__height = value

  def _checkPointCollision(self, position: Vec2, scale: Vec2, rotation: int, point: Vec2) -> bool:
    ##ignore scale and rotation for now
    xInBounds = position.x <= point.x <= position.x + self.__width
    yInBounds = position.y <= point.y <= position.y + self.__height

    return xInBounds and yInBounds


  def _drawDebug(self, displaySurf: Surface, position: Vec2, scale: Vec2, rotation: int):
    rect = Rect(position.x, position.y, self.__width, self.__height )
    draw.rect(displaySurf, (255,0,0), rect, width=3)

    
  
