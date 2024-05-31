from __future__ import annotations
from collections.abc import Sequence
from typing import Type
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from pygame.color import Color
from engine.builder.entity.TextBuilder import TextBuilder
from engine.builder.SceneBuilder import SceneBuilder
from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2


from . import (
    RulesSceneBuilder,
    ChitTutorialSceneBuilder,
    MovementTutorialSceneBuilder,
    WinTutorialSceneBuilder,
)

from ...command.TutorialAdvanceCommand import ChangeTutorialSceneCommand


class TutorialSceneBuilder(SceneBuilder):

    SCENE_BUILDERS: Sequence[Type[SceneBuilder]] = [
        RulesSceneBuilder.RulesSceneBuilder,
        ChitTutorialSceneBuilder.ChitTutorialSceneBuilder,
        MovementTutorialSceneBuilder.MovementTutorialSceneBuilder,
        WinTutorialSceneBuilder.WinTutorialSceneBuilder,
    ]

    def __init__(self) -> None:
        self.__activeScene = 0

    def changeScene(self, amount: int) -> None:
        self.__activeScene = (self.__activeScene + amount) % len(
            TutorialSceneBuilder.SCENE_BUILDERS
        )

    def build(self) -> Scene:
        baseScene = self.SCENE_BUILDERS[self.__activeScene]().build()

        # Add Buttons and Info
        ## Previous
        previousSceneVecPos = Vec2(
            (World().size[0] // 2) - 160, World().size[1] * 7 / 8
        )
        previousSceneButton = (
            ButtonBuilder()
            .setText("<")
            .setOnClick(ChangeTutorialSceneCommand(self, -1))
            .setPosition(previousSceneVecPos)
            .build()
        )
        baseScene.addEntity(previousSceneButton)

        ## Next
        nextSceneVecPos = Vec2((World().size[0] // 2) + 96, World().size[1] * 7 / 8)
        nextSceneButton = (
            ButtonBuilder()
            .setText(">")
            .setOnClick(ChangeTutorialSceneCommand(self, 1))
            .setPosition(nextSceneVecPos)
            .build()
        )
        baseScene.addEntity(nextSceneButton)

        ## Current Scene Text
        infoVecPos = Vec2((World().size[0] // 2) - 32, World().size[1] * 7 / 8)
        infoText = (
            TextBuilder()
            .setPosition(infoVecPos)
            .setText(
                f"{self.__activeScene + 1}/{len(TutorialSceneBuilder.SCENE_BUILDERS)}"
            )
            .setTextColor(Color(0,0,0))
            .setHasRect(False)
            .build()
        )
        baseScene.addEntity(infoText)

        ## Exit to Menu
        from ...builder.scene.MainMenuSceneBuilder import MainMenuSceneBuilder

        exitVecPos = Vec2(64, 64)
        exitButton = (
            ButtonBuilder()
            .setText("Menu")
            .setOnClick(ChangeSceneCommand(MainMenuSceneBuilder()))
            .setPosition(exitVecPos)
            .setRectDetails(164,64)
            .build()
        )
        baseScene.addEntity(exitButton)

        return baseScene
