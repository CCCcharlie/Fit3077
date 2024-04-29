from typing import List
from Engine import Entity


class TurnManager():
  PLAYERS: List[Entity] = []
  ACTIVE_PLAYER: Entity = None
  CURRENT_POSITION = None
