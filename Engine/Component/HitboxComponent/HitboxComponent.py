from ..Component import Component
from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent

class HitboxComponent(Component):
  def __init__(self, owner: Entity, debug=False):
    super().__init__(owner)
    self.debug = debug

  def checkPointCollision(self, x, y):
    tc: TransformComponent = self.owner.get_component(TransformComponent)
    if tc is None:
      return 
    return self._checkPointCollision(tc.x, tc.y, x, y)
  
  def render(self, display_surf):
    if self.debug is False:
      return
    
    tc: TransformComponent = self.owner.get_component(TransformComponent)
    if tc is None:
      return
    
    self._drawDebug(display_surf, tc.x, tc.y)

  def _drawDebug(self, display_surf, x, y):
    raise NotImplementedError("drawDebug must be implemented in subclass")
  

  def _checkPointCollision(self, x, y, point_x, point_y):
    raise NotImplementedError("checkPointCollision must be implemented in subclass")
