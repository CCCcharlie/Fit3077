from dataclasses import dataclass
from fit3077engine.Events.events import Event

from ..Components.components import AnimalType


@dataclass(frozen=True)
class TurnEvent(Event):
    pass


@dataclass(frozen=True)
class ChitEvent(Event):
    animal_type: AnimalType
    count: int
