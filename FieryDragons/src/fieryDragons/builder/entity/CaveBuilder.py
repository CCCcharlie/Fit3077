from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.TrapezoidComponent import TrapezoidComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from typing import List
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType


class CaveBuilder:
    def __init__(self):
        self.__transform: TransformComponent | None = None
        self.__size: int | None = None
        self.__animal_type: AnimalType | None = None
        self.__next: Segment | None = None
        self.__caves: List[Segment] = []
        
    def setTransform(self, transform: TransformComponent) -> CaveBuilder:
        self.__transform = transform
        return self

    def setSize(self, size: int) -> CaveBuilder:
        self.__size = size
        return self

    def setAnimalType(self, animal_type: AnimalType) -> CaveBuilder:
        self.__animal_type = animal_type
        return self
    
    def setNext(self, segment: Segment) -> CaveBuilder:
        self.__next = segment
        return self

    def getCaves(self) -> List[Segment]:
        return self.__caves
        
    def build(self) -> Entity:
        # Error handling
        if self.__transform is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")
        if self.__size is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Size")
        if self.__animal_type is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Animal Type")
        if self.__next is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Next")


        segment = Segment(self.__transform, self.__animal_type, Vec2(0,0))

        self.__next.setCave(segment)    
        segment.setNext(self.__next)


        trap = TrapezoidComponent(
            self.__transform, round(self.__size/2), self.__size, self.__size, self.__animal_type.get_colour()
        )

        e = Entity()
        e.add_renderable(trap)

        self.__caves.append(segment)

        return e
