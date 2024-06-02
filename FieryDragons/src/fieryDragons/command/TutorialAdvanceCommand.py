from __future__ import annotations
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..builder.scene.TutorialSceneBuilder import TutorialSceneBuilder

class ChangeTutorialSceneCommand(ChangeSceneCommand):

    def __init__(self, tutorialBuilder: TutorialSceneBuilder, amount : int):
        self.__tutorialManager = tutorialBuilder
        self.__amount = amount
        super().__init__(tutorialBuilder)

    def run(self):
        self.__tutorialManager.changeScene(self.__amount)
        return super().run()

