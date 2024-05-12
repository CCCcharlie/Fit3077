from typing import List
from engine.utils.SingletonMeta import SingletonMeta
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment


class TurnManager(metaclass=SingletonMeta):
  def __init__(self):
    self.__players: List[Player] = []
    self.__activePlayer = 0

  def register(self, player: Player):
    self.__players.append(player)

  def getActivePlayer(self) -> Player:
    self.__players[self.__activePlayer]

  def nextTurn(self):
    self.__activePlayer = (self.__activePlayer + 1) % len(self.__players)


  def canMove(self, p: Player, position: Segment) -> bool:
     for player in self.__players:
      if (player.getPosition() == position) and (player != p):
        return False
      
      return True



