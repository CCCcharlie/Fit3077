from __future__ import annotations
import random
from enum import Enum
from pygame.color import Color


class AnimalType(Enum):
    SALAMANDER = 0
    SPIDER = 1
    BABY_DRAGON = 2
    BAT = 3
    PIRATE_DRAGON = 4

    def get_colour(self) -> Color:
        match self:
            case AnimalType.SALAMANDER:
                return Color(255, 200, 125)
            case AnimalType.SPIDER:
                return Color(130, 190, 255)
            case AnimalType.BABY_DRAGON:
                return Color(150, 255, 140)
            case AnimalType.BAT:
                return Color(180, 130, 255)
            case AnimalType.PIRATE_DRAGON:
                return Color(150, 150, 150)
            case _:
                return Color(255, 255, 255)

    @classmethod
    def get_random_any(cls) -> AnimalType:
        return random.choice([t for t in AnimalType])

    @classmethod
    def get_random_animal(cls) -> AnimalType:
        # For avoiding PIRATE_DRAGON
        return random.choice(
            [t for t in AnimalType if t is not AnimalType.PIRATE_DRAGON]
        )
