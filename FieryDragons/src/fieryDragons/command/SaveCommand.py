from engine.command.Command import Command
from fieryDragons.save.SaveManager import SaveManager


class SaveCommand(Command):
  def run(self):
    SaveManager().save(0)