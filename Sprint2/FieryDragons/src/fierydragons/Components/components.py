from __future__ import annotations
from enum import Enum
import random

from fit3077engine.ECS.components import (
    ColouredRectangleComponent,
    Component,
    MultiEntityComponent,
    PositionComponent,
    RectangleComponent,
    RelationType,
    Settings,
    SingleEntityComponent,
)
from fit3077engine.ECS.entity import Entity
from fit3077engine.Events.handlers import PygameClickHandler
from fit3077engine.Events.events import ClickEvent, Event
from fit3077engine.Events.observer import ObserverInterface
import pygame
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

    def get_player_id(self, player: Entity) -> int:
        for i, entity in enumerate(self.entities):
            if player is entity:
                return i
        raise ValueError("No such entity on the GameBoard")

    def notify(self, event: Event) -> None:
        pass


class VolcanoLinkComponent(Component):

    def __init__(self, previous: Entity, next: Entity) -> None:
        super().__init__()
        self.previous = previous
        self.next = next

    def get_next_position(self, current_position: Entity, steps: int) -> Entity:
        pass

    def update(self) -> None:
        pass


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


class PlayerRenderComponent(Component):

    RADIUS = 16

    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        screen = Settings.get_instance().screen
        id = (
            list(
                filter(
                    lambda x: x.type is RelationType.PARENT,
                    self._parent.get_components(SingleEntityComponent),
                )
            )[0]
            .entity.get_components(PlayersHandlerComponent)[0]
            .get_player_id(self._parent)
        )

        pos_position_component = self._parent.get_components(PlayerPositionComponent)[
            0
        ].entity.get_components(PositionComponent)[0]

        # Render
        pygame.draw.circle(
            screen,
            Color(255, 255, 255),
            (pos_position_component.x, pos_position_component.y),
            PlayerRenderComponent.RADIUS,
        )
        pygame.draw.circle(
            screen,
            Color(0, 0, 0),
            (pos_position_component.x, pos_position_component.y),
            PlayerRenderComponent.RADIUS + 1,
            3,
        )

        font = pygame.font.Font(None, 32)

        id_text = font.render(str(id), True, Color(0, 0, 0))
        id_text_rect = id_text.get_rect(
            center=(pos_position_component.x, pos_position_component.y)
        )
        screen.blit(id_text, id_text_rect)


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
