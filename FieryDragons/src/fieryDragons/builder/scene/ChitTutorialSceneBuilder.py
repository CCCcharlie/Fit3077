from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.command.DoNothingCommand import DoNothingCommand
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from pygame.color import Color

from ..entity.ChitCardBuilder import ChitCardBuilder


class ChitTutorialSceneBuilder(SceneBuilder):

    TEXT = """In the center of the screen is an example of a Chit Card.
In game these appear in a grid and the aim is to memorise the face-up side of as many cards as possible to gain an advantage.
Each standard Chit Card has a type and a 'count' which are both used to determine player movement.

Chit cards can also have special effects that move the player backwards, shuffle the chit cards in the grid, or swap you with the nearest player.

You can demo clicking the Chit Card now."""

    def __init__(self) -> None:
        super().__init__()
        self.__includeText = True

    def includeText(self, value: bool) -> ChitTutorialSceneBuilder:
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
                ChitTutorialSceneBuilder.TEXT,
                512,
                int(World().size[1] * 6 / 8),
                color=Color(0,0,0)
            )
            e.add_renderable(text)
            scene.addEntity(e)

        # Chit
        chitRadius = 40
        chitVecPos = Vec2(
            (World().size[0] // 2) - (chitRadius // 2),
            (World().size[1] // 2) - (chitRadius // 2),
        )
        chitCard = ChitCardBuilder(chitRadius, None).setPosition(chitVecPos).setCommandOverride(DoNothingCommand()).setAnimate(False).build()
        scene.addEntity(chitCard)

        return scene
