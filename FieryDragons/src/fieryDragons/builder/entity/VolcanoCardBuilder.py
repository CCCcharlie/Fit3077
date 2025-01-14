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
from engine.Random import Random
from fieryDragons.Segment import Segment
from fieryDragons.VolcanoCard import VolcanoCard
from fieryDragons.builder.entity.CaveBuilder import CaveBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.utils.CircleCoordinateIterator import CircleCoordinateIterator
import pygame


class VolcanoCardBuilder:
    def __init__(self):
        # set-able variables
        self.__transform: TransformComponent | None = None
        self.__numSegments: int = None
        self.__hasCave: bool = None
        self.__arcHeight: int | None = None
        self.__arcRadius: int | None = None
        self.__numVolcanoCards: int | None = None

        # Validation variables
        self.__transformChanged = False

        # internal Variables
        self.__previous: VolcanoCard = None
        self.__first: VolcanoCard = None
        self.__screen_width = World().size[0]
        self.__screen_height = World().size[1]
        self.__index = 0

        #builders 
        self.__segmentBuilder: SegmentBuilder = None
        self.__caveBuilder: CaveBuilder = None

    def setArcHeight(self, arcHieght: int) -> VolcanoCardBuilder:
        self.__arcHeight = arcHieght
        return self

    def setArcRadius(self, arcRadius: int) -> VolcanoCardBuilder:
        self.__arcRadius = arcRadius
        return self
    
    def setNumVolcanoCards(self, numVolcanoCards: int) -> VolcanoCardBuilder:
        self.__numVolcanoCards = numVolcanoCards
        return self
    
    def setSegmentBuilder(self, segmentBuilder: SegmentBuilder) -> VolcanoCardBuilder:
        self.__segmentBuilder = segmentBuilder
        return self
    
    def setCaveBuilder(self, caveBuilder: CaveBuilder) -> VolcanoCardBuilder:
        self.__caveBuilder = caveBuilder
        return self

    def setTransform(self, transform: TransformComponent) -> VolcanoCardBuilder:
        self.__transform = transform.clone()
        self.__transformChanged = True
        return self

    def setNumSegments(self, numSegments: int) -> VolcanoCardBuilder:
        self.__numSegments = numSegments
        return self

    def setHasCave(self, hasCave: bool) -> VolcanoCardBuilder:
        self.__hasCave = hasCave
        return self
    
    def getLastVolcanoCard(self) -> VolcanoCard:
        return self.__previous

    def build(self) -> List[Entity]:
        # Error handling
        if self.__transformChanged is False:
            return IncompleteBuilderError(self.__class__.__name__, "Transform Component Unchanged")
        if self.__transform is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")
        if self.__arcHeight is None:
            raise IncompleteBuilderError(self.__class__.__name__, "ArcHeight")
        if self.__arcRadius is None:
            raise IncompleteBuilderError(self.__class__.__name__, "ArcRadius")
        if self.__numVolcanoCards is None:
            raise IncompleteBuilderError(self.__class__.__name__, "NumVolcanoCards")

        self.__transformChanged = False

        # store built entities
        entities = []

        # build trap shape
        trap = CircularSegmentTrapezoidComponent(
            self.__transform, 
            self.__arcHeight,
            self.__arcRadius,
            (360 //self.__numVolcanoCards) - 1,
            pygame.Color(0,0,0),
        )
        e = Entity()
        e.add_renderable(trap)
        entities.append(e)


        # Creation
        segment_iter = CircleCoordinateIterator(
            self.__numVolcanoCards * self.__numSegments,
            self.__arcRadius + 4,
            self.__screen_width // 2,
            self.__screen_height // 2
        )

        transforms = [t for t in segment_iter]
        
        # first create each segment
        segments = []
        for i in range(self.__numSegments):


            transform = transforms[self.__index * (self.__numSegments) + i - 1]

            e = (
                self.__segmentBuilder
                .setAnimalType(AnimalType.get_random_animal())
                .setTransform(transform)
                .build()
            )
            segment = self.__segmentBuilder.getLastSegment()

            entities.append(e)
            segments.append(segment)

        # now create cave if required
        cave = None
        if self.__hasCave:
            # Calculate caves new transform
            caveTransform = self.__transform.clone()
            offset = pygame.Vector2(0,240)
            offset = offset.rotate(-caveTransform.rotation)
            caveTransform.position += Vec2(offset.x, offset.y)

            e = (
                self.__caveBuilder
                .setAnimalType(AnimalType.get_random_animal())
                .setTransform(caveTransform)
                .build()
            )
            cave = self.__caveBuilder.getLastSegment()
            
            entities.append(e)

        vc = VolcanoCard(segments, cave)

        # set the next of the previous volcanoCard and update previous
        if self.__previous:
            self.__previous.setNext(vc)
        self.__previous = vc

        # save first
        if self.__index == 0:
            self.__first = vc

        self.__index += 1

        return entities

    def finish(self):
        self.__previous.setNext(self.__first)
