from __future__ import annotations
from .components import Component
from collections.abc import MutableSequence


class Entity:

    def __init__(self) -> None:
        self.components: MutableSequence[Component] = []

    def update(self) -> None:
        for component in self.components:
            component.update()

    def add_component(self, component: Component) -> "Entity":
        self.components.append(component)
        return self
