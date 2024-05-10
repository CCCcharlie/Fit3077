from abc import abstractmethod
from pygame import Surface
from src.main.engine.Renderable import Renderable
from src.main.engine.utils.Vec2 import Vec2
from src.main.engine.component.TransformComponent import TransformComponent


class HitboxComponent(Renderable):
  """
  base class for hitbox component
  """
  def __init__(self, transformComponent: TransformComponent, debug=False):
    """
    Create a hitbox component

    Args:
      transformComponent (TransformComponent): The transform this hitbox is attached to
      debug (bool): Draw debug hitbox
    """
    self.__transformComponent: TransformComponent = transformComponent
    self.__debug: bool = debug

  def checkPointCollision(self, point: Vec2) -> bool:
    """
    Check point collision 

    Args:
      point (Vec2): The worldspace position of the point to check
    """
    self._checkPointCollision(self.__transformComponent.position, self.__transformComponent.scale, self.__transformComponent.rotation, point)

  def render(self, displaySurf: Surface):
    """
    Render the debug hitbox
    
    Args:
      displaySurf (Surface): The surface to display to
    """
    if self.__debug is False:
      return 

    self._drawDebug(displaySurf, self.__transformComponent.position, self.__transformComponent.scale, self.__transformComponent.rotation)

  @abstractmethod
  def _checkPointCollision(self, position: Vec2, scale: Vec2, rotation: int, point: Vec2) -> bool:
    """
    Check point collision between point and this shape given position, rotation and scale
    
    Args:
      position (Vec2): The position of the hitbox
      scale (Vec2): The scale of the hitbox
      rotation (int): The angle rotation of the hitbox
      point (Vec2): The worldspace position of the point to check
      """
    raise NotImplementedError("_checkPointCollision must be implemented in subclass")
    
  @abstractmethod
  def _drawDebug(self, displaySurf: Surface, position: Vec2, scale: Vec2, rotation: int):
    """
    Draw debug of the hitbox shape

    Args:
      displaySurf (Surface): The surface to display to
      position (Vec2): The position of the hitbox
      scale (Vec2): The scale of the hitbox
      rotation (int): The rotation of the hitbox
    """
    raise NotImplementedError("_drawDebug must be implemented in subclass")
  