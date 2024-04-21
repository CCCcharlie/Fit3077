from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    pass


@dataclass(frozen=True)
class ClickEvent(Event):
    x: int
    y: int
