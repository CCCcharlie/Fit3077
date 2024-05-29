from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2

from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.PlayerBuilder import PlayerBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.enums.AnimalType import AnimalType
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator


class MovementTutorialSceneBuilder(SceneBuilder):

    TEXT = """Players can exist on any Segment of the board.
Movement occurs when a Chit Card is flipped and the type of the card matches the type of the active player's current position.
If the types match then the player advances a number of spaces according to the count of the card.
Otherwise, the player stays put and their turn ends.

Player movement is also prevented when it would cause them to overshoot their home cave or if they would land on the same position as another player.

Click the Chit Card in the middle of the screen to demo player movement."""

    def __init__(self) -> None:
        super().__init__()
        self.__includeText = True

    def includeText(self, value: bool) -> MovementTutorialSceneBuilder:
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
                MovementTutorialSceneBuilder.TEXT,
                512,
                int(World().size[1] * 6 / 8),
            )
            e.add_renderable(text)
            scene.addEntity(e)

        animalType = AnimalType.get_random_animal()
        count = 2

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
        for i, t in zip(range(count + 1), circleIter):
            if i == 0:
                e = (
                    segmentBuilder.setSize(circleIter.size * 1.55)
                    .setTransform(t)
                    .setAnimalType(animalType)
                    .setAnimate(False)
                    .build()
                )
                segment = segmentBuilder.getLastSegment()
            else:
                e = (
                    segmentBuilder.setSize(circleIter.size * 1.55)
                    .setTransform(t)
                    .setAnimalType(None)
                    .setAnimate(False)
                    .build()
                )
            scene.addEntity(e)
        segmentBuilder.finish()

        # Player
        playerBuilder = PlayerBuilder()
        e = playerBuilder.setStartingSegment(segment).setAnimate(False).build()
        playerBuilder.finish()
        scene.addEntity(e)

        return scene
