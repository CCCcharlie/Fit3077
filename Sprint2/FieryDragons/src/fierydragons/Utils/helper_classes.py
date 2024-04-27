from typing import Iterator, Tuple

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
