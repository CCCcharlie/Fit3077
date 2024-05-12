from src.main.fieryDragons.component.ChitCardComponent import ChitCardComponent
from src.main.engine.command import Command


class ChitCardClickedCommand(Command):
  def __init__(self, chitCard: ChitCardComponent):
    self.__chitCard: ChitCardComponent = chitCard
  
  def run(self):
    self.__chitCard.onClick()
    