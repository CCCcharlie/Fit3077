from __future__ import annotations
from typing import TYPE_CHECKING, Type, TypeVar
from collections.abc import MutableSequence, Sequence

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
        component.set_parent(self)
        self.components.append(component)
        return self

    def get_components(self, component_type: Type[C]) -> Sequence[C]:
        components = []
        for component in self.components:
            if isinstance(component, component_type):
                components.append(component)
        return components
