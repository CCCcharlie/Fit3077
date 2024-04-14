import pygame

from Engine.Component.HitboxComponent.HitboxComponent import HitboxComponent
from Engine import Entity


class RectHitboxComponent(HitboxComponent):
    def __init__(self, owner: Entity, width, height, debug=False):
        super().__init__(owner, debug)
        self.width = width
        self.height = height

    def _checkPointCollision(self, x, y, point_x, point_y):
        x_inBounds =  x <= point_x <= x + self.width 
        y_inBounds = y <= point_y <= y + self.height
        return x_inBounds and y_inBounds

    def _drawDebug(self, display_surf, x,y):
        rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(display_surf, (255,0,0), rect, width=3)