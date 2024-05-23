from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command
from fieryDragons.builder.scene.SceneBuilder import SceneBuilder
from fieryDragons.save.SaveManager import SaveManager


class SaveCommand(Command):
  def __init__(self, saveIndex: int, gotoScene: SceneBuilder):
    self.__saveIndex = saveIndex
    self.__gotoScene: SceneBuilder = gotoScene

  def run(self):
    SaveManager().save(self.__saveIndex)
    ##go back to main menu
    ChangeSceneCommand(self.__gotoScene.build()).run()


   