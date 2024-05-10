from pygame import Surface, draw
from main.engine.utils.Vec2 import Vec2
from src.main.engine.component.TransformComponent import TransformComponent
from src.main.engine.component.hitboxComponent.HitboxComponent import HitboxComponent


class CircleHitboxComponent(HitboxComponent):
  """
  Circle hitbox component
  
  For now the scaling and rotation doesn't work
  When it does this will become oval hitbox component :)
  """
  def __init__(self, transformComponent: TransformComponent, radius: int, debug=False):
    """
    Create the hitbox
    
    Args:
      transformComponent (TransformComponent): The transform this hitbox is attached to
      radius (int): The radius of the circle hitbox
      debug (bool): If True will render the hitbox shape
    """
    super().__init__(transformComponent, debug)
    self.__radius = radius

  @property
  def radius(self) -> int:
    return self.__radius
  
  @radius.setter
  def radius(self, value: int):
    self.__radius = value

  def _checkPointCollision(self, position: Vec2, scale: Vec2, rotation: int, point: Vec2) -> bool:
    ##ignore scale and rotation for now
    center = position + Vec2(self.__radius , self.__radius)
    return center.distance(point) <= self.__radius


  def _drawDebug(self, displaySurf: Surface, position: Vec2, scale: Vec2, rotation: int):
    center = position + Vec2(self.__radius , self.__radius)
    draw.circle(displaySurf, (255,0,0), center, self.radius, width=3)
    return super()._drawDebug(displaySurf, position, scale, rotation)
  
