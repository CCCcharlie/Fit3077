from __future__ import annotations
from enum import Enum
import random

from fit3077engine.ECS.components import (
    ColouredRectangleComponent,
    Component,
    MultiEntityComponent,
    RectangleComponent,
    RelationType,
    SingleEntityComponent,
)
from fit3077engine.ECS.entity import Entity
from fit3077engine.Events.handlers import PygameClickHandler
from fit3077engine.Events.events import ClickEvent, Event
from fit3077engine.Events.observer import ObserverInterface
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
                return Color(0, 0, 0)
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


class AnimalTypeComponent(Component):

    def __init__(self, animal_type: AnimalType) -> None:
        super().__init__()
        self.animal_type = animal_type

    def update(self) -> None:
        pass


class ChitRendererComponent(ColouredRectangleComponent):

    CHIT_BACK_COLOUR = Color(80, 50, 40)

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        super().__init__(
            colour=ChitRendererComponent.CHIT_BACK_COLOUR,
            x=x,
            y=y,
            width=width,
            height=height,
        )

    def update(self) -> None:
        flipped = self._parent.get_components(ChitComponent)[0].flipped
        if flipped:
            self.colour = self._parent.get_components(AnimalTypeComponent)[
                0
            ].animal_type.get_colour()
        else:
            self.colour = ChitRendererComponent.CHIT_BACK_COLOUR
        return super().update()


class GameOverComponent(Component):

    def update(self) -> None:
        pass


class PlayersHandlerComponent(MultiEntityComponent, ObserverInterface):

    def __init__(self, *players: Entity) -> None:
        super().__init__(RelationType.CHILD, *players)
        self.current_turn = 0

    def notify(self, event: Event) -> None:
        pass


class BoardPositionComponent(MultiEntityComponent):

    def __init__(
        self, animal_type: AnimalType, is_cave: bool, *next_positions: Entity
    ) -> None:
        super().__init__(RelationType.LINK, *next_positions)
        self.animal_type = animal_type


class ChitComponent(Component, ObserverInterface):

    def __init__(self, count: int) -> None:
        super().__init__()
        self.count = count
        self.flipped = False
        PygameClickHandler.get_instance().add_subscriber(self)

    def update(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        match event:
            case ClickEvent():
                rectangle_components = self._parent.get_components(RectangleComponent)
                for rectangle_component in rectangle_components:
                    rect = rectangle_component.rect
                    if rect.collidepoint(event.x, event.y):
                        self.flipped = not self.flipped
                    return
            case _:
                pass


class PlayerComponent(Component):

    def __init__(self, id: int) -> None:
        super().__init__()
        self.id = id

    def update(self) -> None:
        pass


class PlayerPositionComponent(SingleEntityComponent):

    def __init__(self, start: Entity) -> None:
        super().__init__(RelationType.RELATION, start)
        self.start = start

    def update(self) -> None:
        pass


class PlayerMoveComponent(Component, ObserverInterface):

    def update(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass
