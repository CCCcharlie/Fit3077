
from engine.command.Command import Command
from fieryDragons.ChitCard import ChitCard


class NotifyChitCardInPositionCommand(Command):
  def __init__(self, chitCard: ChitCard):
    self.__chitCard: ChitCard = chitCard
  
  def run(self):
    print("Moving ")
    self.__chitCard.inPosition()
    