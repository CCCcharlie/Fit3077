from __future__ import annotations
from typing import TYPE_CHECKING, Type
from collections.abc import MutableSequence

if TYPE_CHECKING:
    from .components import Component


class Entity:

    def __init__(self) -> None:
        self.components: MutableSequence[Component] = []

    def update(self) -> None:
        for component in self.components:
            component.update()

    def add_component(self, component: Component) -> "Entity":
        component.entity = self
        self.components.append(component)
        return self

    def get_component(self, component_type: Type[Component]) -> Component:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        raise ValueError("No such component on this Entity")
