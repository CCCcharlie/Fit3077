import pygame

from Engine.Component.HitboxComponent.HitboxComponent import HitboxComponent
from Engine import Entity


class CircleHitboxComponent(HitboxComponent):
  def __init__(self, owner: Entity, radius, debug=False):
    super().__init__(owner, debug)
    self.radius = radius

  def _checkPointCollision(self, x, y, point_x, point_y):
    # calcualte centre from x and y
    centreX = x + self.radius
    centreY = y + self.radius

    distance_squared = (point_x - centreX) ** 2 + (point_y - centreY) ** 2
    return distance_squared <= self.radius ** 2

  def _drawDebug(self, display_surf, x, y):
    # calcualte centre from x and y 
    centreX = x + self.radius
    centreY = y + self.radius
    pygame.draw.circle(display_surf, (255,0,0), (centreX, centreY), self.radius, width=3)
