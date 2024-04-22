from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Sequence

from fit3077engine.ECS.entity import Entity

from ..Components.components import AnimalType


class EntityBuilder(ABC):

    @abstractmethod
    def build(self) -> Entity:
        pass


class GameBoardBuilder(EntityBuilder):

    def __init__(self) -> None:
        super().__init__()
        self._players: int = 4
        self._volcano_cards: int = 8
        self._segments: int = 3
        self._chit_cards: int = 16

    def players(self, players: int) -> GameBoardBuilder:
        self._players = players
        return self

    def volcano_cards(self, volcano_cards: int) -> GameBoardBuilder:
        self._volcano_cards = volcano_cards
        return self

    def segments(self, segments: int) -> GameBoardBuilder:
        self._segments = segments
        return self

    def chit_cards(self, chit_cards: int) -> GameBoardBuilder:
        self._chit_cards = chit_cards
        return self

    def build(self) -> Entity:
        game_board = Entity()
        return game_board


class ChitCardBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._animal_type: AnimalType | None = None

    def animal_type(self, animal_type: AnimalType) -> ChitCardBuilder:
        self._animal_type = animal_type
        return self

    def build(self) -> Entity:
        chit_card = Entity()
        return chit_card


class PlayerBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._cave: Entity | None = None

    def start_position(self, start: Entity) -> PlayerBuilder:
        self._cave = start
        return self

    def build(self) -> Entity:
        player = Entity()
        return player


class VolcanoCardBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._animal_types: Sequence[AnimalType] | None = None
        self._cave_type: AnimalType | None = None
        self._x: int | None = None
        self._y: int | None = None

    def segment_types(self, *animal_types: AnimalType) -> VolcanoCardBuilder:
        self._animal_types = [animal_type for animal_type in animal_types]
        return self

    def cave_type(self, animal_type: AnimalType | None) -> VolcanoCardBuilder:
        self._cave_type = animal_type
        return self

    def position(self, x: int, y: int) -> VolcanoCardBuilder:
        self._x = x
        self._y = y
        return self

    def build(self) -> Entity:
        volcano_card = Entity()
        return volcano_card


class PositionBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._animal_type: AnimalType | None = None
        self._x: int | None = None
        self._y: int | None = None

    def animal_type(self, animal_type: AnimalType) -> PositionBuilder:
        self._animal_type = animal_type
        return self

    def position(self, x: int, y: int) -> PositionBuilder:
        self._x = x
        self._y = y
        return self

    def build(self) -> Entity:
        position = Entity()
        return position


class SegmentBuilder(PositionBuilder):

    def build(self) -> Entity:
        segment = super().build()
        return segment


class CaveBuilder(PositionBuilder):

    def build(self) -> Entity:
        cave = super().build()
        return cave
