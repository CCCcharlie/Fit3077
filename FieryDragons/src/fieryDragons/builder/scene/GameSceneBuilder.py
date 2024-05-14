from __future__ import annotations
from typing import List

from engine.scene.Scene import Scene

from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.builder.entity.CaveBuilder import CaveBuilder
from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.utils.GridCoordinateIterator import GridCoordinateIterator
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator


class GameSceneBuilder:
    def __init__(self):
        self.__screen_width = World().size[0]
        self.__screen_height = World().size[1]
        self.__players: int = 4
        ##self.__chit_cards: int  = 24
        self.__segments: int = 16

    def setPlayers(self, players: int) -> GameSceneBuilder:
        self.__players = players
        return self

    # def setChitCards(self, chit_cards: int) -> GameSceneBuilder:
    #     self.__chit_cards = chit_cards
    #     return self

    def setSegments(self, segments: int) -> GameSceneBuilder:
        self.__segments = segments
        return self

    def build(self) -> Scene:
        # Build
        s = Scene()

        # Determine segment-related coordinates
        center_x = self.__screen_width // 2
        center_y = self.__screen_height // 2

        # Place segments
        segment_iter = CircleCoordinateIterator(
            self.__segments,
            5 * min(self.__screen_width, self.__screen_height) // 8,
            center_x,
            center_y,
            offset=1,
        )
        segmentBuilder = SegmentBuilder()
        caveBuilder = CaveBuilder().setRadius(40)


        for index, t in enumerate(segment_iter):
            e = (
                segmentBuilder
                .setSize(segment_iter.size)
                .setTransform(t)
                .setAnimalType(AnimalType.get_random_animal())
                .build()
            )
            s.addEntity(e)

            # Place caves according to player count
            if (index % (self.__segments // self.__players) == 0):
                newTransform = t.clone()
                newTransform.position.x += 100
                newTransform.position.y += 100
                #todo get the generator to handle the further out position
                #todo update the cave generator to pass information to player generator
                c = (
                    caveBuilder
                    .setNext(segmentBuilder.getLastSegment())
                    .setTransform(newTransform)
                    .setAnimalType(AnimalType.get_random_animal())
                    .build()
                )
                s.addEntity(c)
        segmentBuilder.finish()

        #place players
        playerBuilder = PlayerBuilder()
        
        for cave in caveBuilder.getCaves():
            p = playerBuilder.setStartingSegment(cave).build()
            s.addEntity(p)
        playerBuilder.finish()



        # Place chit cards
        gridIterator = GridCoordinateIterator(
            4,
            4,
            Vec2(center_x, center_y),
            min(self.__screen_width, self.__screen_height) // 2,
            min(self.__screen_width, self.__screen_height) // 2,
        )
        chitCardBuilder = ChitCardBuilder(40)

        for v2 in gridIterator:
            e = chitCardBuilder.setPosition(v2).build()
            s.addEntity(e)

        

        return s
