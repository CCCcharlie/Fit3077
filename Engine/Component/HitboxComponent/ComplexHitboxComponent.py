import pygame
from typing import TypedDict, Literal, Dict, Tuple

from Engine.Component.HitboxComponent.HitboxComponent import HitboxComponent
from Engine import Entity


class StoredHitbox(TypedDict):
  hitbox: HitboxComponent
  offset: Tuple[int,int]


class ComplexHitboxComponent(HitboxComponent):
    def __init__(self, owner: Entity, debug=False):
        super().__init__(owner, debug)
        self.hitboxes: Dict[int, StoredHitbox] = {}

    def addHitbox(self, key: str, hitbox: HitboxComponent, offset: Tuple[int,int]):
        if self.hitboxes[key] is not None:
            print(f"overriding hitbox named {key} in complex hitbox")
        self.hitboxes[key] = {'hitbox': hitbox, "offset": offset}

    def removeHitbox(self, key):
        return self.hitboxes.pop(key)

    def _checkPointCollision(self, x, y, point_x, point_y):
        any_hit = False
        for key, storedHitbox in self.hitboxes.items():
            # run check on key
            offset = storedHitbox["offset"]
            hitbox = storedHitbox["hitbox"]

            this_hit = hitbox.checkPointCollision(point_x + offset[0], point_y + offset[1])

            any_hit = any_hit | this_hit

        return any_hit

    def _drawDebug(self, display_surf, x,y):
        for key, storedHitbox in self.hitboxes.items():
            # run check on key
            offset = storedHitbox["offset"]
            hitbox = storedHitbox["hitbox"]

            hitbox.render(display_surf) # todo we should change the offset position some how ??

      
        