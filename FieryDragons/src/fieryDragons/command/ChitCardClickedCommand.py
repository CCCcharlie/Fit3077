from ..ChitCard import ChitCard
from engine.command.Command import Command


class ChitCardClickedCommand(Command):
  def __init__(self, chitCard: ChitCard):
    self.__chitCard: ChitCard = chitCard
  
  def run(self):
    self.__chitCard.onClick()
    