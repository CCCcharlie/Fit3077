from __future__ import annotations

from fit3077engine.Events.handlers import EventHandler

from .event import ChitEvent
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
