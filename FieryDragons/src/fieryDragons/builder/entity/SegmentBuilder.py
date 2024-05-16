from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.SpriteComponent import SpriteComponent
from engine.component.renderable.TrapezoidComponent import TrapezoidComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType
import pygame



class SegmentBuilder:
    def __init__(self):
        self.__transform: TransformComponent | None = None
        self.__size: int | None = None
        self.__animal_type: AnimalType | None = None
        self.__transformChanged = False

        self.__previous: Segment = None
        self.__first: Segment = None
        
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

    
    def finish(self):
        self.__previous.setNext(self.__first)

    def getLastSegment(self) -> Segment:
        return self.__previous
        
    def build(self) -> Entity:
        # Error handling
        if self.__transformChanged is False:
            return IncompleteBuilderError(self.__class__.__name__, "Transform Component Unchanged")
        if self.__transform is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")
        if self.__size is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Size")
        if self.__animal_type is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Animal Type")

        self.__transformChanged = False
        # Creation
        

        segment = Segment(self.__transform, self.__animal_type, Vec2(0,0))
        
        if self.__first is None:
            self.__first = segment
        else:
            self.__previous.setNext(segment)
        self.__previous = segment
        
        

        trap = TrapezoidComponent(
            self.__transform, round(self.__size/2), self.__size, self.__size, self.__animal_type.get_colour()
        )

        transform = self.__transform.clone()
        offset = pygame.Vector2(self.__size/4, 0).rotate(-transform.rotation)
        transform.position = self.__transform.position - Vec2(offset.x, offset.y)

        sprite = SpriteComponent(
            transform, self.__size/2, self.__size/2, self.__animal_type.get_sprite()
        )

        e = Entity()
        e.add_renderable(trap)
        e.add_renderable(sprite)

        return e
