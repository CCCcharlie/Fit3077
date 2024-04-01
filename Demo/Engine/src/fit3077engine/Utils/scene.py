from __future__ import annotations
from collections.abc import MutableSequence
from ..ECS.entity import Entity


class Scene:

    def __init__(self) -> None:
        self.entities: MutableSequence[Entity] = []

    def update(self) -> None:
        for entity in self.entities:
            entity.update()

    def add_entity(self, entity: Entity) -> "Scene":
        self.entities.append(entity)
        return self

    def remove_entity(self, entity: Entity) -> "Scene":
        self.entities.remove(entity)
        return self
