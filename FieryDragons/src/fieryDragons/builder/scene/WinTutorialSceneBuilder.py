from __future__ import annotations
from collections.abc import Sequence
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from pygame.color import Color
from pygame.math import Vector2
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from fieryDragons.builder.entity.CaveBuilder import CaveBuilder
from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.command.MoveActivePlayerCommand import MoveActivePlayerCommand

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

        animalType = AnimalType.SPIDER

        # Chit
        chitRadius = 40
        chitVecPos = Vec2(
            (World().size[0] // 2) - (chitRadius // 2),
            (World().size[1] // 2) - (chitRadius // 2),
        )
        chitCard = (
            ChitCardBuilder(chitRadius, None)
            .setPosition(chitVecPos)
            .setAnimate(False)
            .setAnimalTypeOverride(animalType)
            .setCommandOverride(MoveActivePlayerCommand(animalType, 2))
            .setImageOverride("chitcard/2Spider.png")
            .build()
        )
        scene.addEntity(chitCard)

        # Segments
        segmentBuilder = SegmentBuilder().setSize(200 - 8)

        circleRadius = 1 * min(World().size[0], World().size[1]) // 4 + 25
        center_x = World().size[0] // 2
        center_y = World().size[1] // 2
        c_iter = CircleCoordinateIterator(8 * 3, circleRadius, center_x, center_y)
        segments : Sequence[Segment] = []
        for i in range(4):
            t = next(c_iter)
            segmentBuilder.setAnimalType(
                animalType if i == 0 else AnimalType.get_random_animal()
            )
            scene.addEntity(segmentBuilder.setTransform(t).build())
            # Add Cave Manually
            if i == 2:
                caveTransform = segmentBuilder.getLastSegment().getSnapTransform()
                offset = Vector2(64,32)
                caveTransform.position += Vec2(offset.x, offset.y)
                caveBuilder = CaveBuilder()
                cave = (
                    caveBuilder
                    .setRadius(60)
                    .setAnimalType(AnimalType.get_random_animal())
                    .setTransform(caveTransform)
                    .build()
                )
                segments.append(caveBuilder.getLastSegment())
                scene.addEntity(cave)
            segments.append(segmentBuilder.getLastSegment())

        # Player
        path = segments + segments
        transform = TransformComponent()
        transform.position = path[0].getSnapTransform().position
        r = RectComponent(transform, 50, 50, PlayerBuilder.playerColors[0])
        player_entity = Entity()
        player_entity.add_renderable(r)
        player = Player(path, transform, 0)
        player.setNextPlayer(player)
        Player.ACTIVE_PLAYER = player
        scene.addEntity(player_entity)

        return scene
