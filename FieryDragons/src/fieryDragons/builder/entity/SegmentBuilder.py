from __future__ import annotations

from typing import List, Tuple
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.CircularSegmentTrapezoidComponent import CircularSegmentTrapezoidComponent
from engine.component.renderable.SpriteComponent import SpriteComponent
from engine.component.renderable.TrapezoidComponent import TrapezoidComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.Random import Random
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType
import pygame



class SegmentBuilder:
    def __init__(self):
        self.__transform: TransformComponent | None = None
        self.__size: int | None = None
        self.__animal_type: AnimalType | None = None
        self.__transformChanged: bool = False

        self.__index = 0


    def setTransform(self, transform: TransformComponent) -> SegmentBuilder:
        self.__transform = transform.clone()
        self.__transformChanged = True
        return self
    
    def setSize(self, size: int) -> SegmentBuilder:
        self.__size = size
        return self

    def setAnimalType(self, animal_type: AnimalType) -> SegmentBuilder:
        self.__animal_type = animal_type
        return self

    def getLastSegment(self) -> Segment:
        return self.__lastBuiltSegment
    

    def build(self) -> Entity:
        self.__index += 1
        # Error handling
        if self.__transformChanged is False:
            return IncompleteBuilderError(self.__class__.__name__, "Transform Component Unchanged")
        if self.__transform is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")
        if self.__size is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Size")
        self.__transformChanged = False


        # Creation
        # calculate snap transform from this transform
        snap_transform = self.__transform.clone()
        offset = pygame.Vector2(0,125)
        offset = offset.rotate(-snap_transform.rotation)
        
        snap_transform.position += Vec2(offset.x, offset.y)


        segment = Segment(snap_transform, self.__animal_type)
        self.__lastBuiltSegment = segment

        trap = CircularSegmentTrapezoidComponent(
            self.__transform,
            200 - 8,
            1080 //4 + 29,
            44//3 - 1,
            self.__animal_type.get_colour()
        )

        sprite_transform = self.__transform.clone()
        offset = pygame.Vector2(self.__size/4, 0).rotate(-sprite_transform.rotation)
        sprite_transform.position = self.__transform.position - Vec2(offset.x, offset.y)

        sprite = SpriteComponent(
            sprite_transform, self.__size/2, self.__size/2, self.__animal_type.get_sprite()
        )

        e = Entity()
        e.add_renderable(trap)
        e.add_renderable(sprite)


        # move segments to position in a fanning motion
        start = TransformComponent()
        start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
        start.rotation = self.__transform.rotation
        segmentDelayMove = DelayExecuteMFMFCommand(
        LinearMoveMFCommand(
            start,
            self.__transform.clone(),
            self.__transform, 
            250
        ),
        self.__index * 100
        )
        MultiFrameCommandRunner().addCommand(segmentDelayMove)
        segmentDelayMove.run()

        self.__transform.position = Vec2(-100,-100)

        # this is a hack as the images transform should be an offset as it is a child component
        # of the segment, but this has not been implemented in the engine

        # move segments to position in a fanning motion
        start = TransformComponent()
        start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
        start.rotation = sprite_transform.rotation
        imageDelayMove = DelayExecuteMFMFCommand(
        LinearMoveMFCommand(
            start,
            sprite_transform.clone(),
            sprite_transform, 
            250
        ),
        self.__index * 100
        )
        MultiFrameCommandRunner().addCommand(imageDelayMove)
        imageDelayMove.run()

        sprite_transform.position = Vec2(-100,-100)
        
        return e
