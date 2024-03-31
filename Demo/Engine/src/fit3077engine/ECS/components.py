from .entity import Entity
from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self, parent: Entity) -> None:
        self.entity: Entity = parent

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError()
