from __future__ import annotations
from enum import Enum
from fieryDragons.Random import Random
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

    def get_sprite(self) -> str:
        match self:      
            case AnimalType.SALAMANDER:
                return "chitcard/1Salamander.png"
            case AnimalType.SPIDER:
                return "chitcard/1Spider.png"
            case AnimalType.BABY_DRAGON:
                return "chitcard/1BabyDragon.png"
            case AnimalType.BAT:
                return "chitcard/1Bat.png"
            case AnimalType.PIRATE_DRAGON:
                return "chitcard/1PirateDragon.png"
            case _:
                return ""
    @classmethod
    def get_random_any(cls) -> AnimalType:
        return Random().choice([t for t in AnimalType])

    @classmethod
    def get_random_animal(cls) -> AnimalType:
        return Random().choice(
            [t for t in AnimalType if t is not AnimalType.PIRATE_DRAGON]
        )
