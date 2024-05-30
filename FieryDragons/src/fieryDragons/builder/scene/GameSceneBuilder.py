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
from fieryDragons.builder.entity.VolcanoCardBuilder import VolcanoCardBuilder
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.save.SaveManager import SaveManager
from fieryDragons.utils.GridCoordinateIterator import GridCoordinateIterator
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator


class GameSceneBuilder(SceneBuilder):
    def __init__(self):
        self.__screen_width = World().size[0]
        self.__screen_height = World().size[1]
        self.__numPlayers: int = 2
        self.__numVolcanoCards = 8
        self.__numSegmentPerVolcanoCard = 3

    def setNumPlayers(self, count: int) -> GameSceneBuilder:
        self.__numPlayers = count
        return self

    def setNumVolcanoCards(self, count: int) -> GameSceneBuilder:
        self.__numVolcanoCards = count
        return self
    
    def setNumSegmentPerVolcanoCard(self, count: int) -> GameSceneBuilder:
        self.__numSegmentPerVolcanoCard = count
        return self
  
    def build(self) -> Scene:
        SaveManager().onCleanup()
        # Build
        s = Scene()

        # Determine segment-related coordinates
        center_x = self.__screen_width // 2
        center_y = self.__screen_height // 2 + 40

        # Create iterators 
        segment_iter = CircleCoordinateIterator(
            self.__numVolcanoCards,
            5 * min(self.__screen_width, self.__screen_height) // 8 - 150,
            center_x,
            center_y,
            offset=1,
        )

        #Create builders
        segmentBuilder = SegmentBuilder().setSize(segment_iter.size * 1.55)
        caveBuilder = CaveBuilder().setRadius(40)
        playerBuilder = PlayerBuilder()

        volcanoCardBuilder = (
            VolcanoCardBuilder()
            .setArcHeight(40)
            .setCaveBuilder(caveBuilder)
            .setSegmentBuilder(segmentBuilder)
            .setNumSegments(self.__numSegmentPerVolcanoCard)
        )

        # build volcano cards saving built caves
        builtCaves = []

        for index, t in enumerate(segment_iter):
            # Determine if this vc has a cave
            hasCave: bool = (index % (self.__numVolcanoCards // self.__numPlayers)) == 0
       
            # add this volcano card 
            es = (
                volcanoCardBuilder
                .setTransform(t)
                .setHasCave(hasCave)
                .build()
            )

            for e in es:
                s.addEntity(e)

            if hasCave:
             builtCaves.append(volcanoCardBuilder.getLastVolcanoCard())

        volcanoCardBuilder.finish()

        #place players
        for vc in builtCaves:
            p = playerBuilder.setStartingVolcanoCard(vc).build()
            s.addEntity(p)
        playerBuilder.finish()

        # Place chit cards
        gridIterator = GridCoordinateIterator(
            4,
            4,
            Vec2(center_x + 20, center_y),
            min(self.__screen_width, self.__screen_height) // 2,
            min(self.__screen_width, self.__screen_height) // 2,
        )
        chitCardBuilder = ChitCardBuilder(40)

        for v2 in gridIterator:
            e = chitCardBuilder.setPosition(v2).build()
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
