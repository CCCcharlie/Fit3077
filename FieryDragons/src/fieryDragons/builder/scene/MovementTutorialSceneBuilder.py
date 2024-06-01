from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from pygame.color import Color
from fieryDragons.Player import Player

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
                color=Color(0, 0, 0),
            )
            e.add_renderable(text)
            scene.addEntity(e)

        animalType = AnimalType.get_random_animal()

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
            .build()
        )
        scene.addEntity(chitCard)

        # Segments
        segmentBuilder = SegmentBuilder().setSize(200-8)

        circleRadius = 1 * min(World().size[0], World().size[1]) // 4 + 25
        center_x = World().size[0] // 2
        center_y = World().size[1] // 2
        c_iter = CircleCoordinateIterator(8*3, circleRadius, center_x, center_y)
        segments = []
        for i in range(4):
            segmentBuilder.setAnimalType(animalType if i == 0 else AnimalType.get_random_animal())
            scene.addEntity(segmentBuilder.setTransform(next(c_iter)).build())
            segments.append(segmentBuilder.getLastSegment())

        # Player
        path = segments + segments
        transform = TransformComponent()
        transform.position = path[0].getSnapTransform().position
        r = RectComponent(transform, 50,50,PlayerBuilder.playerColors[0])
        player_entity = Entity()
        player_entity.add_renderable(r)
        player = Player(path, transform, 0)
        player.setNextPlayer(player)
        Player.ACTIVE_PLAYER = player
        scene.addEntity(player_entity)

        return scene
