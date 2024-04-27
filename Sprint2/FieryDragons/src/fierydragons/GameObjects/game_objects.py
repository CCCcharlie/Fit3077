from __future__ import annotations
from abc import abstractmethod
from collections.abc import MutableSequence, Sequence
from random import randint
from typing import Tuple
import pygame
from pygame.color import Color
from pygame.rect import Rect

from fit3077engine.GameObjects.game_objects import GameObject
from fit3077engine.GameObjects.interfaces import RenderableInterface
from fit3077engine.Events.observer import ObserverInterface
from fit3077engine.Events.events import Event
from fit3077engine.Utils.settings import Settings

from .enums import AnimalType
from ..Utils.enums import Side
from ..Utils.helper_classes import RectangleGridIterator, SegmentedSquareIterator


class GameBoard(GameObject, ObserverInterface):

    current_instance: GameBoard | None = None

    def __init__(
        self, segments: int = 24, players: int = 4, chit_cards: int = 16
    ) -> None:
        super().__init__()
        settings = Settings.get_instance()
        self.x, self.y = (
            (settings.screen.get_width() // 2) - (settings.screen.get_height() // 2),
            0,
        )
        self.size = settings.screen.get_height()

        self.segments, caves, pos_size = self._place_segments(segments, players)
        self.players = self._create_players(caves)
        self._current_turn = 0
        self.chit_cards = self._create_chit_cards(chit_cards, int(pos_size * 2.5))

        GameBoard.current_instance = self

    def _place_segments(
        self, segments: int, players: int
    ) -> Tuple[Sequence[SegmentPosition], Sequence[CavePosition], int]:
        settings = Settings.get_instance()

        segments_list: MutableSequence[SegmentPosition] = []
        caves_list: MutableSequence[CavePosition] = []
        board_iter = SegmentedSquareIterator(
            self.x, self.y, self.size, segments, offset=1
        )
        for seg_idx, (x, y, side) in zip(range(segments), board_iter):

            if (seg_idx - 1) % (segments // players) == 0:
                # Segment should have a cave
                cave_type = AnimalType(len(caves_list) % len(AnimalType))
            else:
                # No Cave
                cave_type = None

            new_segment = SegmentPosition(x, y, board_iter.size, side, cave_type)
            segments_list.append(new_segment)
            if new_segment.cave is not None:
                caves_list.append(new_segment.cave)

        # Link Segments
        for seg_idx, seg in enumerate(segments_list):
            prev_seg = segments_list[(seg_idx - 1) % len(segments_list)]
            next_seg = segments_list[(seg_idx + 1) % len(segments_list)]
            seg.link(prev_seg, next_seg)

        return segments_list, caves_list, board_iter.size

    def _create_players(self, caves: Sequence[CavePosition]) -> Sequence[Player]:
        players: MutableSequence[Player] = []

        for cave in caves:
            players.append(Player(cave))

        return players

    def _create_chit_cards(self, amount: int, gap: int) -> Sequence[ChitCard]:
        chit_cards: MutableSequence[ChitCard] = []

        x_start, y_start = self.x + gap, self.y + gap
        chit_iterator = RectangleGridIterator(
            x_start, y_start, self.size - (2 * gap), (5, 7), amount, 2
        )
        for x, y in chit_iterator:
            new_chit = ChitCard(x, y, chit_iterator.width, chit_iterator.height)
            chit_cards.append(new_chit)

        return chit_cards

    @classmethod
    def get_instance(cls) -> GameBoard:
        if cls.current_instance is None:
            raise ValueError(f"{GameBoard.__name__} not instantiated.")
        return cls.current_instance

    def player_id(self, player: Player) -> int:
        for id, list_player in enumerate(self.players):
            if player is list_player:
                return id
        raise ValueError("That Player is not active on this board.")

    def is_player_turn(self, player: Player) -> bool:
        return self.player_id(player) == self._current_turn

    def update(self) -> None:
        for segment in self.segments:
            segment.update()
        for player in self.players:
            player.update()
        for chit_card in self.chit_cards:
            chit_card.update()

    def notify(self, event: Event) -> None:
        pass


class Player(GameObject, RenderableInterface, ObserverInterface):

    def __init__(self, cave: CavePosition) -> None:
        super().__init__()
        self.position: GamePosition = cave
        self.cave = cave

    def update(self) -> None:
        self.render()

    def render(self) -> None:
        id = GameBoard.get_instance().player_id(self)
        screen = Settings.get_instance().screen
        x, y = self.position.rect.center
        RADIUS = 16

        if GameBoard.get_instance().is_player_turn(self):
            colour = Color(255, 0, 0)
        else:
            colour = Color(255, 255, 255)

        # Circle
        pygame.draw.circle(screen, colour, (x, y), RADIUS)  # Colour
        pygame.draw.circle(
            screen, Color(0, 0, 0), (x, y), RADIUS, RADIUS // 4
        )  # Outline
        # ID Number
        font = pygame.font.Font(None, RADIUS * 2)
        id_text = font.render(str(id + 1), True, Color(0, 0, 0))
        id_text_rect = id_text.get_rect(center=(x, y))
        screen.blit(id_text, id_text_rect)

    def notify(self, event: Event) -> None:
        pass


class GamePosition(GameObject, RenderableInterface):

    def __init__(self, x: int, y: int, size: int, animal_type: AnimalType) -> None:
        super().__init__()
        self.rect = Rect(x, y, size, size)
        self.animal_type = animal_type

    @abstractmethod
    def next(self, player: Player) -> GamePosition | None:
        pass

    @abstractmethod
    def previous(self, player: Player) -> GamePosition | None:
        pass

    def render(self) -> None:
        screen = Settings.get_instance().screen
        pygame.draw.rect(screen, self.animal_type.get_colour(), self.rect)  # Colour
        pygame.draw.rect(screen, (0, 0, 0), self.rect, self.rect.width // 8)  # Outline


class SegmentPosition(GamePosition):

    def __init__(
        self, x: int, y: int, size: int, side: Side, cave_type: AnimalType | None = None
    ) -> None:
        super().__init__(x, y, size, AnimalType.get_random_animal())
        self._previous: SegmentPosition = None
        self._next: SegmentPosition = None
        self._create_cave(side, cave_type)

    def _create_cave(self, side: Side, cave_type: AnimalType | None) -> None:
        self.cave: CavePosition | None = None
        if cave_type is not None:
            match side:
                case Side.TOP:
                    cave_x = self.rect.x
                    cave_y = self.rect.y - self.rect.width
                case Side.RIGHT:
                    cave_x = self.rect.x + self.rect.width
                    cave_y = self.rect.y
                case Side.BOTTOM:
                    cave_x = self.rect.x
                    cave_y = self.rect.y + self.rect.width
                case Side.LEFT:
                    cave_x = self.rect.x - self.rect.width
                    cave_y = self.rect.y
            self.cave = CavePosition(cave_x, cave_y, self.rect.width, cave_type)

    def update(self) -> None:
        if self.cave is not None:
            self.cave.update()
        self.render()

    def link(self, previous: SegmentPosition, next: SegmentPosition) -> None:
        self._previous = previous
        self._next = next

    def next(self, player: Player) -> GamePosition | None:
        return super().next(player)

    def previous(self, player: Player) -> GamePosition | None:
        return super().previous(player)


class CavePosition(GamePosition):

    def __init__(self, x: int, y: int, size: int, animal_type: AnimalType) -> None:
        super().__init__(x, y, size, animal_type)
        self._next: GamePosition = None

    def update(self) -> None:
        self.render()

    def link(self, next: GamePosition) -> None:
        self._next = next

    def next(self, player: Player) -> GamePosition | None:
        return super().next(player)

    def previous(self, player: Player) -> GamePosition | None:
        return super().previous(player)

    def render(self) -> None:
        return super().render()


class ChitCard(GameObject, RenderableInterface, ObserverInterface):

    MIN_COUNT = 1
    MAX_COUNT = 3

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.count = randint(ChitCard.MIN_COUNT, ChitCard.MAX_COUNT)
        self.animal_type = AnimalType.get_random_any()
        self.flipped = False

    def update(self) -> None:
        self.render()

    def render(self) -> None:
        screen = Settings.get_instance().screen
        OUTLINE_RATIO = 8

        # Card
        pygame.draw.rect(screen, self.animal_type.get_colour(), self.rect)  # Colour
        pygame.draw.rect(
            screen, Color(0, 0, 0), self.rect, self.rect.width // OUTLINE_RATIO
        )  # Outline

        # Count
        font = pygame.font.Font(None, self.rect.width)
        count_text = font.render(str(self.count), True, Color(0, 0, 0))
        count_text_rect = count_text.get_rect(center=self.rect.center)
        screen.blit(count_text, count_text_rect)

    def notify(self, event: Event) -> None:
        pass
