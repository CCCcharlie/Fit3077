from engine.command.Command import Command
from fieryDragons.save.SaveManager import SaveManager


class SaveCommand(Command):
  def __init__(self, saveIndex: int):
    self.__saveIndex = saveIndex

  def run(self):
    SaveManager().save(self.__saveIndex)
   