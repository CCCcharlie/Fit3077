from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.TrapezoidComponent import TrapezoidComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from fieryDragons.enums.AnimalType import AnimalType



class SegmentBuilder:
    def __init__(self):
        self.__transform: TransformComponent | None = None
        self.__size: int | None = None
        self.__animal_type: AnimalType | None = None
        self.__transformChanged = False

    def setTransform(self, transform: TransformComponent) -> SegmentBuilder:
        self.__transform = transform
        self.__transformChanged = True
        return self

    def setSize(self, size: int) -> SegmentBuilder:
        self.__size = size
        return self

    def setAnimalType(self, animal_type: AnimalType) -> SegmentBuilder:
        self.__animal_type = animal_type
        return self

    def build(self) -> Entity:
        # Error handling
        if self.__transformChanged is None:
            return IncompleteBuilderError(self.__class__.__name__, "Transform Component Unchanged")
        if self.__transform is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")
        if self.__size is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Size")
        if self.__animal_type is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Animal Type")

        self.__transformChanged = False
        # Creation

        trap = TrapezoidComponent(
            self.__transform, round(self.__size/2), self.__size, self.__size, self.__animal_type.get_colour()
        )

        e = Entity()
        e.add_renderable(trap)

        return e
