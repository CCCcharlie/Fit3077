from typing import Iterator, Tuple
from math import ceil, sqrt

from fit3077engine.GameObjects.interfaces import UpdateableInterface
from fit3077engine.Utils.settings import Settings

from .enums import Side


class SegmentedSquareIterator(Iterator[Tuple[int, int, Side]]):

    def __init__(
        self, x: int, y: int, size: int, segments: int, offset: int = 0
    ) -> None:
        self.segments = segments
        self._segment = 0
        self._segments_placed = 0

        self._segments_per_side = ((segments - 2) // 4) + 2
        self.size = size // (self._segments_per_side + 2 * offset)
        self.side = Side.TOP

        self._size = size - (2 * offset * self.size)
        self.x = x + offset * self.size
        self.y = y + offset * self.size

    def __iter__(self) -> Iterator[Tuple[int, int, Side]]:
        return self

    def __next__(self) -> Tuple[int, int, Side]:
        if self._segments_placed == self.segments:
            raise StopIteration()

        result = (self.x, self.y, self.side)

        # Update Values
        if self._segment < self._segments_per_side - 1:
            self._segment += 1
        else:
            self._segment = 1
            self.side = Side((self.side.value + 1) % len(Side))

        match self.side:
            case Side.TOP:
                self.x += self.size
            case Side.RIGHT:
                self.y += self.size
            case Side.BOTTOM:
                self.x -= self.size
            case Side.LEFT:
                self.y -= self.size

        self._segments_placed += 1
        return result


class RectangleGridIterator(Iterator[Tuple[int, int]]):

    def __init__(
        self,
        x: int,
        y: int,
        size: int,
        ratio: Tuple[int, int],
        tiles: int,
        gap_ratio: int,
    ) -> None:
        self._cols_rows = ceil(sqrt(tiles))
        effective_cols_rows = self._cols_rows + ceil((self._cols_rows - 1) / gap_ratio)

        # Size Handling
        if ratio[0] > ratio[1]:
            self.width = ceil(size / effective_cols_rows)
            self.height = ceil((self.width * ratio[1]) / ratio[0])
        else:
            self.height = ceil(size / effective_cols_rows)
            self.width = ceil((self.height * ratio[0]) / ratio[1])

        self.w_gap = self.width // gap_ratio
        self.h_gap = self.height // gap_ratio

        # Recentering
        width_diff = size - (self.width * effective_cols_rows)
        height_diff = size - (self.height * effective_cols_rows)
        self.x = x + (width_diff // 2)
        self._x_start = x + (width_diff // 2)
        self.y = y + height_diff // 2

        # Iteration
        self.tiles = tiles
        self._tiles_placed = 0
        self._tile = 0

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        return self

    def __next__(self) -> Tuple[int, int]:
        if self._tiles_placed == self.tiles:
            raise StopIteration()

        result = (self.x, self.y)

        # Update Values
        if self._tile < self._cols_rows - 1:
            self._tile += 1
            self.x += self.width + self.w_gap
        else:
            self._tile = 0
            self.x = self._x_start
            self.y += self.height + self.h_gap

        self._tiles_placed += 1
        return result


class Timer(UpdateableInterface):

    def __init__(self, seconds: float) -> None:
        self.timing = False
        self._start_frames = int(seconds * Settings.get_instance().fps)
        self._frames = 0

    def start(self) -> None:
        self.timing = True
        self._frames = self._start_frames

    def check(self) -> bool:
        if self.timing and self._frames <= 0:
            self.timing = False
            return True
        return False

    def update(self) -> None:
        if self.timing:
            self._frames = max(0, self._frames - 1)
