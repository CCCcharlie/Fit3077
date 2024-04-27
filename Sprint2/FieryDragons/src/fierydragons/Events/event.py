from dataclasses import dataclass
from fit3077engine.Events.events import Event

from ..GameObjects.enums import AnimalType


@dataclass(frozen=True)
class ChitEvent(Event):
    animal_type: AnimalType
    count: int
    turn: int
