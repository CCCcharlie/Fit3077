from __future__ import annotations
from fit3077engine.Events.handlers import EventHandler

from fierydragons.Utils.enums import AnimalType
from .events import ChitEvent, TurnEvent


class TurnEventHandler(EventHandler):
    instance: TurnEventHandler | None = None

    def __init__(self) -> None:
        if TurnEventHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {TurnEventHandler.__name__} more than once. Use get_instance()"
            )
        super().__init__()

    @classmethod
    def get_instance(cls) -> TurnEventHandler:
        if cls.instance is None:
            cls.instance = TurnEventHandler()
        return cls.instance

    def emit(self) -> None:
        self._emit(TurnEvent())


class ChitFlipHandler(EventHandler):
    instance: ChitFlipHandler | None = None

    def __init__(self) -> None:
        if ChitFlipHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {ChitFlipHandler.__name__} more than once. Use get_instance()"
            )
        super().__init__()

    @classmethod
    def get_instance(cls) -> ChitFlipHandler:
        if cls.instance is None:
            cls.instance = ChitFlipHandler()
        return cls.instance

    def emit(self, animal_type: AnimalType, count: int) -> None:
        self._emit(ChitEvent(animal_type, count))
