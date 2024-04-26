from __future__ import annotations
from collections.abc import Sequence
import sys
from typing import Tuple

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
from fierydragons.Events.events import ChitEvent, TurnEvent
from fierydragons.Events.handlers import ChitFlipHandler, TurnEventHandler
from fierydragons.Utils.enums import AnimalType


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
        chit_component = self._parent.get_components(ChitComponent)[0]
        flipped = chit_component.flipped
        if flipped or True:
            self.colour = self._parent.get_components(AnimalTypeComponent)[
                0
            ].animal_type.get_colour()

        else:
            self.colour = ChitRendererComponent.CHIT_BACK_COLOUR
        super().update()

        # Count
        if flipped:
            count = chit_component.count
            font = pygame.font.Font(None, 32)
            count_text = font.render(str(count), True, Color(0, 0, 0))
            count_text_rect = count_text.get_rect(center=self.rect.center)
            Settings.get_instance().screen.blit(count_text, count_text_rect)


class GameOverComponent(Component):

    def update(self) -> None:
        players = self._parent.get_components(PlayersHandlerComponent)[0].entities

        for player in players:
            position_component = player.get_components(PlayerPositionComponent)[0]
            move_component = player.get_components(PlayerMoveComponent)[0]
            if (
                move_component.steps > 0
                and position_component.entity is position_component.start
            ):
                pygame.quit()
                sys.exit(0)


class PlayersHandlerComponent(MultiEntityComponent, ObserverInterface):

    def __init__(self, *players: Entity) -> None:
        super().__init__(RelationType.CHILD, *players)
        self.current_turn = 0
        TurnEventHandler.get_instance().add_subscriber(self)

    def get_player_id(self, player: Entity) -> int:
        for i, entity in enumerate(self.entities):
            if player is entity:
                return i
        raise ValueError("No such entity on the GameBoard")

    def is_player_turn(self, player: Entity) -> bool:
        return self.get_player_id(player) == self.current_turn

    def notify(self, event: Event) -> None:
        match event:
            case TurnEvent():
                self.current_turn = (self.current_turn + 1) % len(self.entities)
            case _:
                pass


class VolcanoLinkComponent(Component):

    def __init__(self, previous: Entity, next: Entity) -> None:
        super().__init__()
        self.previous = previous
        self.next = next

    def update(self) -> None:
        pass


class PositionLinkComponent(Component):

    def __init__(
        self,
        *,
        previous: Sequence[Tuple[Entity, bool]] | None,
        next: Sequence[Tuple[Entity, bool]] | None,
    ) -> None:
        self._previous = previous
        self._next = next

    @property
    def previous(self) -> Sequence[Tuple[Entity, bool]]:
        if self._previous is not None:
            return self._previous
        else:
            return [
                (
                    list(
                        filter(
                            lambda x: x.type is RelationType.PARENT,
                            self._parent.get_components(SingleEntityComponent),
                        )
                    )[0]
                    .entity.get_components(VolcanoLinkComponent)[0]
                    .previous.get_components(MultiEntityComponent)[0]
                    .entities[-1],
                    False,
                )
            ]

    @property
    def next(self) -> Sequence[Tuple[Entity, bool]]:
        if self._next is not None:
            return self._next
        else:
            return [
                (
                    list(
                        filter(
                            lambda x: x.type is RelationType.PARENT,
                            self._parent.get_components(SingleEntityComponent),
                        )
                    )[0]
                    .entity.get_components(VolcanoLinkComponent)[0]
                    .next.get_components(MultiEntityComponent)[0]
                    .entities[0],
                    False,
                )
            ]

    def update(self) -> None:
        pass


class ChitComponent(Component, ObserverInterface):

    def __init__(self, count: int) -> None:
        super().__init__()
        self.count = count
        self.flipped = False
        self.emit_in = None
        PygameClickHandler.get_instance().add_subscriber(self)
        TurnEventHandler.get_instance().add_subscriber(self)

    def update(self) -> None:
        if self.emit_in is not None:
            if self.emit_in > 0:
                self.emit_in -= 1
            else:
                self._emit_flip()
                self.emit_in = None

    def _emit_flip(self) -> None:
        animal_type = self._parent.get_components(AnimalTypeComponent)[0].animal_type
        count = self.count
        ChitFlipHandler.get_instance().emit(animal_type, count)

    def notify(self, event: Event) -> None:
        match event:
            case ClickEvent():
                rectangle_components = self._parent.get_components(RectangleComponent)
                for rectangle_component in rectangle_components:
                    rect = rectangle_component.rect
                    if rect.collidepoint(event.x, event.y) and not self.flipped:
                        self.flipped = True
                        self.emit_in = 60
                    return
            case TurnEvent():
                self.flipped = False
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
        ) + 1

        pos_position_component = self._parent.get_components(PlayerPositionComponent)[
            0
        ].entity.get_components(PositionComponent)[0]

        # Render
        player_handler = list(
            filter(
                lambda x: x.type is RelationType.PARENT,
                self._parent.get_components(SingleEntityComponent),
            )
        )[0].entity.get_components(PlayersHandlerComponent)[0]
        if player_handler.current_turn == player_handler.get_player_id(self._parent):
            player_color = Color(255, 0, 0)
        else:
            player_color = Color(255, 255, 255)
        pygame.draw.circle(
            screen,
            player_color,
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

    def __init__(self) -> None:
        super().__init__()
        self.steps = 0
        self.end_turn = None
        ChitFlipHandler.get_instance().add_subscriber(self)

    def update(self) -> None:
        if self.end_turn is not None:
            if self.end_turn > 0:
                self.end_turn -= 1
            else:
                self.end_turn = None
                TurnEventHandler.get_instance().emit()

    def _handle_move(self, animal_type: AnimalType, count: int) -> None:
        game_board = list(
            filter(
                lambda x: x.type is RelationType.PARENT,
                self._parent.get_components(SingleEntityComponent),
            )
        )[0].entity
        player_handler = game_board.get_components(PlayersHandlerComponent)[0]
        position_component = self._parent.get_components(PlayerPositionComponent)[0]
        position = position_component.entity
        position_animal_type = position.get_components(AnimalTypeComponent)[
            0
        ].animal_type

        if player_handler.is_player_turn(self._parent):
            if (
                position_animal_type is animal_type
                or animal_type is AnimalType.PIRATE_DRAGON
            ):
                match animal_type:
                    case AnimalType.PIRATE_DRAGON:
                        steps = -count
                    case _:
                        steps = count
                new_position = self._traverse_to_position(steps, position)
                if new_position is not None:
                    position_component.entity = new_position
                    if new_position is position_component.start:
                        self.end_turn = 60
                else:
                    self.end_turn = 60
                if steps < 0:
                    self.end_turn = 60
            else:
                self.end_turn = 60

    def _traverse_to_position(self, steps: int, start: Entity) -> Entity | None:
        current = start
        start_cave = self._parent.get_components(PlayerPositionComponent)[0].start

        while steps != 0:
            link = current.get_components(PositionLinkComponent)[0]

            if steps < 0:
                steps += 1
                self.steps = max(self.steps - 1, 0)
                if len(link.previous) == 0:
                    return None
                for position, is_cave in link.previous:
                    if is_cave and position is start_cave:
                        return position
                    elif not is_cave:
                        current = position

            if steps > 0:
                steps -= 1
                self.steps += 1
                for position, is_cave in link.next:
                    if position is start_cave:
                        if is_cave and steps == 0:
                            return position
                        elif is_cave and steps > 0:
                            return None
                    current = position

        return current

    def notify(self, event: Event) -> None:
        match event:
            case ChitEvent():
                self._handle_move(event.animal_type, event.count)
            case _:
                pass
