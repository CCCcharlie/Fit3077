from enum import Enum
from dataclasses import dataclass


class EventType(Enum):
    QUIT = 0


@dataclass(frozen=True)
class Event:
    type: EventType
