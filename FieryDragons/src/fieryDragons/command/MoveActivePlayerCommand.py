from typing import Dict
from engine.command.Command import Command
from fieryDragons.Player import Player
from fieryDragons.enums.AnimalType import AnimalType

class MoveActivePlayerCommand(Command):
  def __init__(self, animalType: AnimalType, amount: int):
    self.__animalType = animalType
    self.__amount = amount

  def run(self):
    if Player.ACTIVE_PLAYER is not None:
        Player.ACTIVE_PLAYER.move(self.__animalType, self.__amount)
