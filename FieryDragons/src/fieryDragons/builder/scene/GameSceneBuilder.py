from __future__ import annotations
from typing import List

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene

from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.builder.entity.ActivePlayerDisplayBuilder import ActivePlayerDisplayBuilder
from fieryDragons.builder.entity.CaveBuilder import CaveBuilder
from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SavePopupBuilder import SavePopupBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from engine.builder.SceneBuilder import SceneBuilder
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.save.SaveManager import SaveManager
from fieryDragons.utils.GridCoordinateIterator import GridCoordinateIterator
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator


class GameSceneBuilder(SceneBuilder):
    def __init__(self):
        self.__screen_width = World().size[0]
        self.__screen_height = World().size[1]
        self.__players: int = 2
        ##self.__chit_cards: int  = 24
        self.__segments: int = 24

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
        SaveManager().onCleanup()
        # Build
        s = Scene()

        # Determine segment-related coordinates
        center_x = self.__screen_width // 2
        center_y = self.__screen_height // 2 + 40

        # Place segments
        segment_iter = CircleCoordinateIterator(
            self.__segments,
            5 * min(self.__screen_width, self.__screen_height) // 8 - 150,
            center_x,
            center_y,
            offset=1,
        )
        segmentBuilder = SegmentBuilder()
        caveBuilder = CaveBuilder().setRadius(40)


        for index, t in enumerate(segment_iter):
            e = (
                segmentBuilder
                .setSize(segment_iter.size * 1.55)
                .setTransform(t)
                .build()
            )
            s.addEntity(e)

            # Place caves according to player count
            if (index % (self.__segments // self.__players) == 0):
                c = (
                    caveBuilder
                    .setNext(segmentBuilder.getLastSegment())
                    .setSegmentSize(segment_iter.size + 30)
                    .setSegmentTransform(t)
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
            5,
            4,
            Vec2(center_x + 20, center_y),
            min(self.__screen_width, self.__screen_height) // 2,
            min(self.__screen_width, self.__screen_height) // 2,
        )
        chitCardBuilder = ChitCardBuilder(40)

        for v2 in gridIterator:
            if not chitCardBuilder.has_more_cards():
                break
            e = chitCardBuilder.setPosition(v2).build()
            if e is not None:
                s.addEntity(e)


        #place active player render
        apdBuilder = ActivePlayerDisplayBuilder().setPlayerColors(PlayerBuilder.playerColors)
        s.addEntity(apdBuilder.build())

        # add save popop
        savePopupBuilder = SavePopupBuilder()
        es: List[Entity] = savePopupBuilder.build()

        for e in es:
            s.addEntity(e)

        # add restartButton
        # late import to prevent circular dep
        from fieryDragons.command.LoadGameCommand import LoadGameCommand
        restartButtonBuilder = (
            ButtonBuilder()
            .setText("Restart")
            .setPosition(Vec2(1500, 300))
            .setRectDetails(200,50)
            .setOnClick(LoadGameCommand())
        )

        s.addEntity(restartButtonBuilder.build())


        return s
