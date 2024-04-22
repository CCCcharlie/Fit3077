from enum import Enum

from fit3077engine.ECS.components import (
    Component,
    MultiEntityComponent,
    RelationType,
    SingleEntityComponent,
)
from fit3077engine.ECS.entity import Entity
from fit3077engine.Events.events import Event
from fit3077engine.Events.observer import ObserverInterface


class AnimalType(Enum):
    SALAMANDER = 0
    SPIDER = 1
    BABY_DRAGON = 2
    BAT = 3
    PIRATE_DRAGON = 4


class AnimalTypeComponent(Component):

    def __init__(self, animal_type: AnimalType) -> None:
        super().__init__()
        self.animal_type = animal_type

    def update(self) -> None:
        pass


class GameOverComponent(Component):

    def update(self) -> None:
        pass


class PlayerPositionComponent(SingleEntityComponent):

    def __init__(self, position: Entity, start: Entity) -> None:
        super().__init__(RelationType.RELATION, position)
        self.start = start

    def update(self) -> None:
        pass


class PlayersHandlerComponent(MultiEntityComponent, ObserverInterface):

    def __init__(self, *players: Entity) -> None:
        super().__init__(RelationType.CHILD, *players)
        self.current_turn = 0

    def notify(self, event: Event) -> None:
        pass


class BoardPositionComponent(MultiEntityComponent):

    def __init__(self, animal_type: AnimalType, *next_positions: Entity) -> None:
        super().__init__(RelationType.LINK, *next_positions)
        self.animal_type = animal_type


class ChitComponent(Component, ObserverInterface):

    def __init__(self, count: int) -> None:
        super().__init__()
        self.count = count
        self.flipped = False

    def update(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass


class PlayerMoveComponent(Component, ObserverInterface):

    def update(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass
