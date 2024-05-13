from typing import Iterator
from math import pi, sin, cos

from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2


class CircleCoordinateIterator(Iterator[TransformComponent]):

    def __init__(
        self, elements: int, radius: int, center_x: int, center_y: int, offset: int = 0
    ) -> None:
        self.size = (radius * 2) // ((elements + 4 * offset) // 2)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__elements = elements
        self.__n = 0
        self.__radius = radius - self.size * (
            offset + 1
        )  # Center point exists on the inner circle

    def __iter__(self) -> Iterator[TransformComponent]:
        return self

    def __next__(self) -> TransformComponent:
        # End after all elements placed
        if self.__n >= self.__elements:
            raise StopIteration()

        # Calculate angle at current iteration
        angle = pi * 2 * self.__n / self.__elements

        # Calculate coords based on current angle
        x = self.__radius * cos(angle)
        y = self.__radius * sin(angle)

        # calculate rotation
        rot = round(angle)

        # Update counter
        self.__n += 1

        # Return result, offsetting for top left square position and centering
        t = TransformComponent()
        t.position = Vec2(
            x - (self.size / 2) + self.__center_x, y - (self.size / 2) + self.__center_y
        )
        t.rotation = rot
        return t
