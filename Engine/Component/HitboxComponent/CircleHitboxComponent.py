import pygame

from Engine.Component.HitboxComponent.HitboxComponent import HitboxComponent
from Engine import Entity


class CircleHitboxComponent(HitboxComponent):
  def __init__(self, owner: Entity, radius, debug=False):
    super().__init__(owner, debug)
    self.radius = radius

  def _checkPointCollision(self, x, y, point_x, point_y):
    distance_squared = (point_x - x) ** 2 + (point_y - y) ** 2
    return distance_squared <= self.radius ** 2

  def _drawDebug(self, display_surf, x, y):
    pygame.draw.circle(display_surf, (255,0,0), (x,y), self.radius, width=3)
