from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from pygame.color import Color
from fieryDragons.Player import Player
from fieryDragons.builder.entity.CaveBuilder import CaveBuilder
from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder

from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.utils.CircleCoordinateIterator import CircleCoordinateIterator


class WinTutorialSceneBuilder(SceneBuilder):

    TEXT = """The player wins when their movement aligns with returning to their home cave.
The cave placed in this tutorial is marked as the tutorial player's home.
You can flip the chit card again to move to the cave and complete the tutorial."""

    def __init__(self) -> None:
        super().__init__()
        self.__includeText = True

    def includeText(self, value: bool) -> WinTutorialSceneBuilder:
        self.__includeText = value
        return self

    def build(self) -> Scene:
        scene = Scene()

        # Text
        if self.__includeText:
            e = Entity()
            textPos = TransformComponent()
            textPos.position = Vec2(World().size[0] * 1 / 16, World().size[1] * 1 / 8)
            text = ParagraphComponent(
                textPos,
                WinTutorialSceneBuilder.TEXT,
                512,
                int(World().size[1] * 6 / 8),
                color=Color(0, 0, 0),
            )
            e.add_renderable(text)
            scene.addEntity(e)

        animalType = AnimalType.get_random_animal()
        count = 3

        # Chit
        chitRadius = 40
        chitVecPos = Vec2(
            (World().size[0] // 2) - (chitRadius // 2),
            (World().size[1] // 2) - (chitRadius // 2),
        )
        chitCard = (
            ChitCardBuilder(chitRadius)
            .setPosition(chitVecPos)
            .setAnimate(False)
            .setAnimalType(animalType)
            .setCount(count)
            .build()
        )
        scene.addEntity(chitCard)

        # Segments
        circleIter = CircleCoordinateIterator(
            24,
            5 * min(*World().size) // 8 - 150,
            World().size[0] // 2,
            World().size[1] // 2 + 40,
            offset=1,
        )
        segmentBuilder = SegmentBuilder()
        segments = []
        for i, t in zip(range(count), circleIter):
            if i == 0:
                e = (
                    segmentBuilder.setSize(circleIter.size * 1.55)
                    .setTransform(t)
                    .setAnimalType(animalType)
                    .setAnimate(False)
                    .build()
                )
                start = segmentBuilder.getLastSegment()
            else:
                e = (
                    segmentBuilder.setSize(circleIter.size * 1.55)
                    .setTransform(t)
                    .setAnimalType(None)
                    .setAnimate(False)
                    .build()
                )
            segments.append(segmentBuilder.getLastSegment())
            scene.addEntity(e)
        segmentBuilder.finish()

        # Cave
        caveBuilder = (
            CaveBuilder()
            .setRadius(40)
            .setNext(segmentBuilder.getLastSegment())
            .setSegmentSize(circleIter.size + 30)
            .setSegmentTransform(t)
            .setAnimate(False)
            .setAnimalType(AnimalType.get_random_animal())
        )
        scene.addEntity(caveBuilder.build())
        cave = caveBuilder.getCaves()[0]
        segments.append(cave)

        # Player
        playerBuilder = PlayerBuilder()
        e = playerBuilder.setStartingSegment(start).setAnimate(False).build()
        playerBuilder.finish()
        scene.addEntity(e)
        player = Player.ACTIVE_PLAYER
        player.path = segments + [segments[0]]

        return scene
