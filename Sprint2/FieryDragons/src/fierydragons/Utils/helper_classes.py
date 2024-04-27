from typing import Iterator, Tuple
from math import ceil, sqrt

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
        self.x = x
        self._x_start = x
        self.y = y

        self._cols = ceil(sqrt((tiles * ratio[1]) / ratio[0]))
        effective_cols = self._cols + ceil((self._cols - 1) / gap_ratio)

        self.width = size // effective_cols
        self.height = (self.width * ratio[1]) // ratio[0]
        self.w_gap = self.width // gap_ratio
        self.h_gap = self.height // gap_ratio

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
        if self._tile < self._cols - 1:
            self._tile += 1
            self.x += self.width + self.w_gap
        else:
            self._tile = 0
            self.x = self._x_start
            self.y += self.height + self.h_gap

        self._tiles_placed += 1
        return result
