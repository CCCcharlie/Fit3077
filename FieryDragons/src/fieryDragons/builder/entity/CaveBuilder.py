from __future__ import annotations
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.CircleComponent import CircleComponent
from engine.component.renderable.SpriteComponent import SpriteComponent
from engine.component.renderable.TrapezoidComponent import TrapezoidComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from typing import List
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType
from pygame import Color
import pygame


class CaveBuilder:
    def __init__(self):
        self.__transform: TransformComponent | None = None
        self.__radius: int | None = None
        self.__animal_type: AnimalType | None = None
        self.__next: Segment | None = None
        self.__caves: List[Segment] = []
        self.__segmentSize: int = 0

    def setSegmentSize(self, segSize: int) -> CaveBuilder:
        self.__segmentSize = segSize
        return self
        
    def setSegmentTransform(self, transform: TransformComponent) -> CaveBuilder:
        newTransform = transform.clone()

        moveDistance = pygame.Vector2(0,self.__segmentSize)
        offset = moveDistance.rotate(-newTransform.rotation)

        newPos = newTransform.position + Vec2(offset.x, offset.y)
        newTransform.position = newPos

        self.__transform = newTransform
        return self

    def setRadius(self, radius: int) -> CaveBuilder:
        self.__radius = radius
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
        if self.__radius is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Radius")
        if self.__animal_type is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Animal Type")
        if self.__next is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Next")


        segment = Segment(self.__transform, self.__animal_type, Vec2(0,0))

        self.__next.setCave(segment)    
        segment.setNext(self.__next)

        cave = CircleComponent(
            self.__transform, self.__radius, self.__animal_type.get_colour(),Color(0,0,0)
        )

        transform = self.__transform.clone()
        offset = pygame.Vector2(self.__radius, self.__radius).rotate(-transform.rotation)
        transform.position = transform.position - Vec2(offset.x, offset.y)

        sprite = SpriteComponent(
            transform,2 * self.__radius, 2 * self.__radius, self.__animal_type.get_sprite()
        )
    

        e = Entity()
        e.add_renderable(cave)
        e.add_renderable(sprite)

        self.__caves.append(segment)

        return e
