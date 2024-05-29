from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2


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

        return scene
