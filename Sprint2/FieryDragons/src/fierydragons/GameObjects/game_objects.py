from __future__ import annotations
from abc import abstractmethod
from collections.abc import MutableSequence, Sequence

from fit3077engine.GameObjects.game_objects import GameObject
from fit3077engine.GameObjects.interfaces import RenderableInterface
from fit3077engine.Events.observer import ObserverInterface
from fit3077engine.Events.events import Event
from fit3077engine.Utils.settings import Settings
import pygame
from pygame.rect import Rect

from .enums import AnimalType
from ..Utils.enums import Side
from ..Utils.helper_classes import SegmentedSquareIterator


class GameBoard(GameObject, ObserverInterface):

    current_instance: GameBoard | None = None

    def __init__(
        self, segments: int = 24, players: int = 4, chit_cards: int = 16
    ) -> None:
        super().__init__()

        self.segments = self._place_segments(segments, players)

        self.current_instance = self

    def _place_segments(self, segments: int, players: int) -> Sequence[SegmentPosition]:
        settings = Settings.get_instance()

        segments_list: MutableSequence[SegmentPosition] = []
        caves = 0
        top_left_x, top_left_y = (
            (settings.screen.get_width() // 2) - (settings.screen.get_height() // 2),
            0,
        )
        board_iter = SegmentedSquareIterator(
            top_left_x, top_left_y, settings.screen.get_height(), segments, offset=1
        )
        for seg_idx, (x, y, side) in zip(range(segments), board_iter):
            if seg_idx % (segments // players) == 0:
                # Segment should have a cave
                segments_list.append(
                    SegmentPosition(
                        x, y, board_iter.size, side, AnimalType(caves % len(AnimalType))
                    )
                )
                caves += 1
            else:
                # No Cave
                segments_list.append(
                    SegmentPosition(
                        x,
                        y,
                        board_iter.size,
                        side,
                    )
                )
        # Link Segments
        for seg_idx, seg in enumerate(segments_list):
            prev_seg = segments_list[(seg_idx - 1) % len(segments_list)]
            next_seg = segments_list[(seg_idx + 1) % len(segments_list)]
            seg.link(prev_seg, next_seg)

        return segments_list

    @classmethod
    def get_instance(cls) -> GameBoard:
        if cls.current_instance is None:
            raise ValueError(f"{GameBoard.__name__} not instantiated.")
        return cls.current_instance

    def update(self) -> None:
        for segment in self.segments:
            segment.update()

    def notify(self, event: Event) -> None:
        pass


class Player(GameObject, RenderableInterface, ObserverInterface):

    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

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
        pass

    def link(self, next: GamePosition) -> None:
        self._next = next

    def next(self, player: Player) -> GamePosition | None:
        return super().next(player)

    def previous(self, player: Player) -> GamePosition | None:
        return super().previous(player)

    def render(self) -> None:
        return super().render()


class ChitCard(GameObject, RenderableInterface, ObserverInterface):

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass
