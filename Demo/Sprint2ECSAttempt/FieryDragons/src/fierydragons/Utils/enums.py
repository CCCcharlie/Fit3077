from __future__ import annotations
from enum import Enum
import random

from pygame.color import Color


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class AnimalType(Enum):
    SALAMANDER = 0
    SPIDER = 1
    BABY_DRAGON = 2
    BAT = 3
    PIRATE_DRAGON = 4

    def get_colour(self) -> Color:
        match self:
            case AnimalType.SALAMANDER:
                return Color(255, 100, 0)
            case AnimalType.SPIDER:
                return Color(0, 0, 255)
            case AnimalType.BABY_DRAGON:
                return Color(0, 255, 0)
            case AnimalType.BAT:
                return Color(100, 20, 130)
            case AnimalType.PIRATE_DRAGON:
                return Color(150, 150, 150)
            case _:
                return Color(255, 255, 255)

    @classmethod
    def get_random_any(cls) -> AnimalType:
        return random.choice([t for t in AnimalType])

    @classmethod
    def get_random_animal(cls) -> AnimalType:
        return random.choice(
            [t for t in AnimalType if t is not AnimalType.PIRATE_DRAGON]
        )
