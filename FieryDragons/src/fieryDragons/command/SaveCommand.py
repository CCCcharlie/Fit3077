from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command

from fieryDragons.save.SaveManager import SaveManager


class SaveCommand(Command):
  def __init__(self, saveIndex: int):
    self.__saveIndex = saveIndex

  def run(self):
    ## late import to prevent circular dependency
    from fieryDragons.builder.scene.MainMenuSceneBuilder import MainMenuSceneBuilder
    mainMenuSceneBuilder = MainMenuSceneBuilder()

    SaveManager().save(self.__saveIndex)
    
    ##go back to main menu
    ChangeSceneCommand(mainMenuSceneBuilder).run()


   