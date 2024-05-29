from __future__ import annotations
from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2


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
                textPos, WinTutorialSceneBuilder.TEXT, 512, int(World().size[1] * 6 / 8)
            )
            e.add_renderable(text)
            scene.addEntity(e)

        return scene
