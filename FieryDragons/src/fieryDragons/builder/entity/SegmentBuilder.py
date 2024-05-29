from __future__ import annotations

from typing import List, Tuple
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
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
        self.__transformChanged = False

        self.__previous: Segment = None
        self.__first: Segment = None

        self.__index = 0

        self.__animate = True

        ## define volcano cards
        volcanoCardSpecifications: List[Tuple[AnimalType, AnimalType, AnimalType]] = [
            (AnimalType.BABY_DRAGON, AnimalType.BAT, AnimalType.SPIDER),
            (AnimalType.SALAMANDER, AnimalType.SPIDER, AnimalType.BAT),
            (AnimalType.SPIDER, AnimalType.SALAMANDER, AnimalType.BABY_DRAGON),
            (AnimalType.BAT, AnimalType.SPIDER, AnimalType.BABY_DRAGON),
            (AnimalType.SPIDER, AnimalType.BAT, AnimalType.SALAMANDER),
            (AnimalType.BABY_DRAGON, AnimalType.SALAMANDER, AnimalType.BAT),
            (AnimalType.BAT, AnimalType.BABY_DRAGON, AnimalType.SALAMANDER),
            (AnimalType.SALAMANDER, AnimalType.BABY_DRAGON, AnimalType.SPIDER)
        ]
        
        Random().shuffle(volcanoCardSpecifications)
        # extract order from specs 
        self._volcanoCardTypes: List[AnimalType] = []
        for a,b,c in volcanoCardSpecifications:
            self._volcanoCardTypes.append(a)
            self._volcanoCardTypes.append(b)
            self._volcanoCardTypes.append(c)

        
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

    def setAnimate(self, value : bool) -> SegmentBuilder:
        self.__animate = value
        return self
    
    def finish(self):
        self.__previous.setNext(self.__first)

    def getLastSegment(self) -> Segment:
        return self.__previous
        
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
        
        if self.__animal_type is None:
            self.__animal_type = self._volcanoCardTypes.pop(0)

        segment = Segment(self.__transform, self.__animal_type, Vec2(0,0))
        
        if self.__first is None:
            self.__first = segment
        else:
            self.__previous.setNext(segment)
        self.__previous = segment
        
        

        trap = TrapezoidComponent(
            self.__transform, round(3 * self.__size/4 - 10), self.__size+ 10, self.__size, self.__animal_type.get_colour()
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


        if self.__animate:
            # move segments to position in a fanning motion
            start = TransformComponent()
            start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
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
            imageDelayMove = DelayExecuteMFMFCommand(
            LinearMoveMFCommand(
                start,
                transform.clone(),
                transform, 
                250
            ),
            self.__index * 100
            )
            MultiFrameCommandRunner().addCommand(imageDelayMove)
            imageDelayMove.run()

            transform.position = Vec2(-100,-100)

        # Reset animal type
        self.__animal_type = None
        
        return e
