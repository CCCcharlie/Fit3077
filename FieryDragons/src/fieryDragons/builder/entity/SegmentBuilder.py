from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from engine.component.renderable.RectComponent import RectComponent
from ...utils.AnimalType import AnimalType

class SegmentBuilder:

    def __init__(self):
        self.__position : Vec2 | None = None
        self.__size : int | None = None
        self.__animal_type : AnimalType | None = None

    def setPosition(self, position: Vec2) -> SegmentBuilder:
        self.__position = position
        return self

    def setSize(self, size : int) -> SegmentBuilder:
        self.__size = size
        return self

    def setAnimalType(self, animal_type : AnimalType) -> SegmentBuilder:
        self.__animal_type = animal_type
        return self

    def build(self) -> Entity:
        # Error handling 
        if self.__position is None: raise IncompleteBuilderError(self.__class__.__name__, "Position")
        if self.__size is None: raise IncompleteBuilderError(self.__class__.__name__, "Size")
        if self.__animal_type is None: raise IncompleteBuilderError(self.__class__.__name__, "Animal Type")

        tc = TransformComponent()
        tc.position = self.__position
        square = RectComponent(tc, self.__size, self.__size, self.__animal_type.get_colour()) 
        
        e = Entity()
        e.add_renderable(square)

        return e
