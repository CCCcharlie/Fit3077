from engine.command.Command import Command
from fieryDragons.TurnManager import TurnManager
from fieryDragons.enums.AnimalType import AnimalType


class MoveActivePlayerCommand(Command):
  def __init__(self, animalType: AnimalType, amount: int):
    self.__animalType = animalType
    self.__amount = amount

  def run(self):
    TurnManager().getActivePlayer().move(self.__animalType, self.__amount)