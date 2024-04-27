from dataclasses import dataclass
from fit3077engine.Events.events import Event

from fierydragons.GameObjects import game_objects

from ..GameObjects.enums import AnimalType


@dataclass(frozen=True)
class ChitEvent(Event):
    animal_type: AnimalType
    count: int
    turn: int


@dataclass(frozen=True)
class TurnEndEvent(Event):
    pass


@dataclass(frozen=True)
class GameOverEvent(Event):
    player: "game_objects.Player"
