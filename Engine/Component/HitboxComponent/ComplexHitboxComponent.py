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
        hits = []
        for key, storedHitbox in self.hitboxes.items():
            # run check on key
            offset = storedHitbox["offset"]
            hitbox = storedHitbox["hitbox"]


            this_hit = hitbox.checkPointCollision(point_x + offset[0], point_y + offset[1])
            if this_hit:
                hits.append(key)

        print(f"Hits are {hits}") #todo somehow return which ones were hit
        return len(hits) > 0

    def _drawDebug(self, display_surf, x,y):
        for key, storedHitbox in self.hitboxes.items():
            # run check on key
            offset = storedHitbox["offset"]
            hitbox = storedHitbox["hitbox"]

            hitbox._drawDebug(display_surf, x + offset[0], y + offset[1])
     

      
        