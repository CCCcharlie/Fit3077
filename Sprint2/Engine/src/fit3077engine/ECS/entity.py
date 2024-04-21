from __future__ import annotations
from typing import TYPE_CHECKING, Type, TypeVar
from collections.abc import MutableSequence

if TYPE_CHECKING:
    from .components import Component

C = TypeVar("C", bound=Component)


class Entity:

    def __init__(self) -> None:
        self.components: MutableSequence[Component] = []

    def update(self) -> None:
        for component in self.components:
            component.update()

    def add_component(self, component: Component) -> "Entity":
        component.parent = self
        self.components.append(component)
        return self

    def get_component(self, component_type: Type[C]) -> C:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        raise ValueError("No such component on this Entity")
