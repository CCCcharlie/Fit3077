from __future__ import annotations

from fit3077engine.Events.handlers import EventHandler

from .event import ChitEvent, TurnEndEvent
from ..GameObjects.enums import AnimalType
from ..GameObjects import game_objects


class ChitFlipHandler(EventHandler):

    instance: ChitFlipHandler | None = None

    def __init__(self) -> None:
        super().__init__()
        if ChitFlipHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {ChitFlipHandler.__name__} more than once. Use get_instance()"
            )
        ChitFlipHandler.instance = self

    @classmethod
    def get_instance(cls) -> ChitFlipHandler:
        if cls.instance is None:
            cls.instance = ChitFlipHandler()
        return cls.instance

    def emit(self, animal_type: AnimalType, count: int) -> None:
        current_turn = game_objects.GameBoard.get_instance().turns_passed
        self._emit(ChitEvent(animal_type, count, current_turn))


class TurnEndHandler(EventHandler):

    instance: TurnEndHandler | None = None

    def __init__(self) -> None:
        super().__init__()
        if TurnEndHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {TurnEndHandler.__name__} more than once. Use get_instance()"
            )
        TurnEndHandler.instance = self

    @classmethod
    def get_instance(cls) -> TurnEndHandler:
        if cls.instance is None:
            cls.instance = TurnEndHandler()
        return cls.instance

    def emit(self) -> None:
        self._emit(TurnEndEvent())
