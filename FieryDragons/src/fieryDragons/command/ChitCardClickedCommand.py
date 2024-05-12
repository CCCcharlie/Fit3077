from ..component.ChitCardComponent import ChitCardComponent
from engine.command.Command import Command


class ChitCardClickedCommand(Command):
  def __init__(self, chitCard: ChitCardComponent):
    self.__chitCard: ChitCardComponent = chitCard
  
  def run(self):
    self.__chitCard.onClick()
    