from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import MutableSequence, Sequence
from random import randint
from math import ceil, sqrt
from fit3077engine.ECS.components import (
    ColouredRectangleComponent,
    MultiEntityComponent,
    PositionComponent,
    RelationType,
    SingleEntityComponent,
)

from fit3077engine.ECS.entity import Entity
from fit3077engine.Utils.settings import Settings
from pygame.color import Color

from ..Utils.enums import Direction

from ..Components.components import (
    AnimalType,
    AnimalTypeComponent,
    ChitComponent,
    ChitRendererComponent,
    PlayerMoveComponent,
    PlayerPositionComponent,
    PlayersHandlerComponent,
)


class EntityBuilder(ABC):

    @abstractmethod
    def build(self) -> Entity:
        pass


class GameBoardBuilder(EntityBuilder):

    def __init__(self) -> None:
        super().__init__()
        self._players: int = 4
        self._volcano_cards: int = 8
        self._segments: int = 3
        self._chit_cards: int = 16

    def players(self, players: int) -> GameBoardBuilder:
        self._players = players
        return self

    def volcano_cards(self, volcano_cards: int) -> GameBoardBuilder:
        self._volcano_cards = volcano_cards
        return self

    def segments(self, segments: int) -> GameBoardBuilder:
        self._segments = segments
        return self

    def chit_cards(self, chit_cards: int) -> GameBoardBuilder:
        self._chit_cards = chit_cards
        return self

    def build(self) -> Entity:
        game_board = Entity()
        settings = Settings.get_instance()
        # Main Components
        x, y = (
            (settings.screen.get_width() // 2) - (settings.screen.get_height() // 2),
            0,
        )  # Board as a square in the middle of the screen
        width, height = (settings.screen.get_height(), settings.screen.get_height())
        game_board.add_component(PositionComponent(x, y))

        # Relational Components
        ## Volcano Cards
        pos_size = max(width, height) // (
            ((self._volcano_cards // 4) * self._segments) + 3
        )
        vc_list: MutableSequence[Entity] = []
        cave_list: MutableSequence[Entity] = []
        vc_x, vc_y = x + pos_size, y + pos_size
        direction = Direction.RIGHT
        vc_width, vc_height = pos_size * self._segments, pos_size
        for card_no in range(self._volcano_cards):
            ### Caves
            if card_no % (self._volcano_cards // self._players) == 0:
                cave_type = AnimalType(len(cave_list) % len(AnimalType))
                match direction:
                    case Direction.UP:
                        cave_direction = Direction.LEFT
                    case Direction.DOWN:
                        cave_direction = Direction.RIGHT
                    case Direction.LEFT:
                        cave_direction = Direction.DOWN
                    case Direction.RIGHT:
                        cave_direction = Direction.UP
                    case _:
                        raise ValueError("Invalid direction")
            else:
                cave_type = None
                cave_direction = None

            ### Volcano Card Building
            vc = (
                VolcanoCardBuilder()
                .segments(self._segments)
                .position(vc_x, vc_y)
                .dimensions(vc_width, vc_height)
                .cave(cave_type, cave_direction)
                .build()
            )
            if len(vc_list) > 0:
                vc_list[-1].add_component(SingleEntityComponent(RelationType.LINK, vc))
            vc_list.append(vc)

            ### Store Cave
            if cave_type is not None and cave_direction is not None:
                cave_list.append(vc.get_components(SingleEntityComponent)[0].entity)

            ### Next Coords
            match direction:
                case Direction.UP:
                    vc_y -= vc_height
                case Direction.DOWN:
                    vc_y += vc_height
                    if vc_y + vc_height > (y + height) - (2 * pos_size):
                        direction = Direction.LEFT
                        vc_x -= (self._segments - 1) * pos_size
                        vc_width, vc_height = vc_height, vc_width
                case Direction.LEFT:
                    if vc_x - vc_width < x + pos_size:
                        direction = Direction.UP
                        vc_x -= pos_size
                        vc_y -= (self._segments - 1) * pos_size
                        vc_width, vc_height = vc_height, vc_width
                    else:
                        vc_x -= vc_width
                case Direction.RIGHT:
                    vc_x += vc_width
                    if vc_x + vc_width > (x + width) - (2 * pos_size):
                        direction = Direction.DOWN
                        vc_width, vc_height = vc_height, vc_width

        vc_list[-1].add_component(
            SingleEntityComponent(RelationType.LINK, vc_list[0])
        )  # Wrap around link

        game_board.add_component(MultiEntityComponent(RelationType.CHILD, *vc_list))

        ## Players
        player_list: MutableSequence[Entity] = []
        for player_no in range(self._players):
            player = PlayerBuilder().cave(cave_list[player_no]).build()
            player_list.append(player)

        game_board.add_component(PlayersHandlerComponent(*player_list))

        ## Chit Cards
        chit_list = []
        chit_x, chit_y = x + (3 * pos_size), y + (3 * pos_size)
        chit_ratio = 5 / 7
        chit_cols = ceil(sqrt(self._chit_cards))
        chit_width = (width - 6 * pos_size) // (chit_cols + ceil((chit_cols - 1) / 2))
        chit_height = int((1 / chit_ratio) * chit_width)
        chits_remaining = self._chit_cards
        while chits_remaining > 0:
            chit_x = x + (3 * pos_size)
            for col in range(min(chit_cols, chits_remaining)):
                chit = (
                    ChitCardBuilder()
                    .animal_type(AnimalType.get_random_any())
                    .count(randint(1, 3))
                    .position(chit_x, chit_y)
                    .dimensions(chit_width, chit_height)
                    .build()
                )
                chit_list.append(chit)
                chits_remaining -= 1

                chit_x += int(1.5 * chit_width)

            chit_y += int(chit_height + (chit_width / 2))

        game_board.add_component(MultiEntityComponent(RelationType.CHILD, *chit_list))

        return game_board


class ChitCardBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._animal_type: AnimalType | None = None
        self._count: int | None = None
        self._x: int | None = None
        self._y: int | None = None
        self._width: int | None = None
        self._height: int | None = None

    def animal_type(self, animal_type: AnimalType) -> ChitCardBuilder:
        self._animal_type = animal_type
        return self

    def count(self, count: int) -> ChitCardBuilder:
        self._count = count
        return self

    def position(self, x: int, y: int) -> ChitCardBuilder:
        self._x = x
        self._y = y
        return self

    def dimensions(self, width: int, height: int) -> ChitCardBuilder:
        self._width = width
        self._height = height
        return self

    def build(self) -> Entity:
        if (
            self._animal_type is None
            or self._count is None
            or self._x is None
            or self._y is None
            or self._width is None
            or self._height is None
        ):
            raise ValueError("All builder fields must be provided with a value.")
        chit_card = (
            Entity()
            .add_component(ChitComponent(self._count))
            .add_component(AnimalTypeComponent(self._animal_type))
            .add_component(
                ChitRendererComponent(self._x, self._y, self._width, self._height),
            )
        )
        return chit_card


class PlayerBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._start: Entity | None = None

    def cave(self, cave: Entity) -> PlayerBuilder:
        self._start = cave
        return self

    def build(self) -> Entity:
        if self._start is None:
            raise ValueError("All builder fields must be provided with a value.")
        player = (
            Entity()
            .add_component(PlayerPositionComponent(self._start))
            .add_component(PlayerMoveComponent())
        )
        return player


class VolcanoCardBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._segments: int = 3
        self._cave_type: AnimalType | None = None
        self._cave_direction: Direction | None = None
        self._x: int | None = None
        self._y: int | None = None
        self._width: int | None = None
        self._height: int | None = None

    def segments(self, segments: int) -> VolcanoCardBuilder:
        self._segments = segments
        return self

    def cave(
        self,
        animal_type: AnimalType | None,
        direction: Direction | None,
    ) -> VolcanoCardBuilder:
        self._cave_type = animal_type
        self._cave_direction = direction
        return self

    def position(self, x: int, y: int) -> VolcanoCardBuilder:
        self._x = x
        self._y = y
        return self

    def dimensions(self, width: int, height: int) -> VolcanoCardBuilder:
        self._width = width
        self._height = height
        return self

    def build(self) -> Entity:
        if (
            self._x is None
            or self._y is None
            or self._width is None
            or self._height is None
        ):
            raise ValueError("All builder fields must be provided with a value.")

        border = int(0.30 * min(self._width, self._height))

        pos_size = min(self._height, self._width) - border

        volcano_card = (
            Entity()
            .add_component(
                ColouredRectangleComponent(
                    Color(0, 0, 0),
                    x=self._x,
                    y=self._y,
                    width=self._width,
                    height=self._height,
                )
            )
            .add_component(PositionComponent(self._x, self._y))
        )

        # Place Segments
        segments_list: MutableSequence[Entity] = []
        seg_x, seg_y = self._x + (border // 2), self._y + (border // 2)
        for segment_no in range(self._segments):
            segment = (
                SegmentBuilder()
                .dimensions(pos_size, pos_size)
                .animal_type(AnimalType.get_random_animal())
                .position(seg_x, seg_y)
                .build()
            )

            segments_list.append(segment)

            ## Coords Update
            seg_x += pos_size + border
            seg_y += pos_size + border

        volcano_card.add_component(
            MultiEntityComponent(RelationType.CHILD, *segments_list)
        )

        # Place Cave
        if self._cave_type is not None and self._cave_direction is not None:
            cave_builder = (
                CaveBuilder()
                .dimensions(pos_size, pos_size)
                .animal_type(self._cave_type)
            )

            cave_segment_pos = segments_list[len(segments_list) // 2].get_components(
                PositionComponent
            )[0]

            match self._cave_direction:
                case Direction.UP:
                    cave_x, cave_y = (
                        cave_segment_pos.x,
                        cave_segment_pos.y - pos_size - border,
                    )
                case Direction.DOWN:
                    cave_x, cave_y = (
                        cave_segment_pos.x,
                        cave_segment_pos.y + pos_size + border,
                    )
                case Direction.LEFT:
                    cave_x, cave_y = (
                        cave_segment_pos.x - pos_size - border,
                        cave_segment_pos.y,
                    )
                case Direction.RIGHT:
                    cave_x, cave_y = (
                        cave_segment_pos.x + pos_size + border,
                        cave_segment_pos.y,
                    )

            cave_builder.position(cave_x, cave_y)

            volcano_card.add_component(
                SingleEntityComponent(RelationType.CHILD, cave_builder.build())
            )

        return volcano_card


class PositionBuilder(EntityBuilder):

    def __init__(self) -> None:
        self._animal_type: AnimalType | None = None
        self._x: int | None = None
        self._y: int | None = None
        self._width: int | None = None
        self._height: int | None = None

    def animal_type(self, animal_type: AnimalType) -> PositionBuilder:
        self._animal_type = animal_type
        return self

    def position(self, x: int, y: int) -> PositionBuilder:
        self._x = x
        self._y = y
        return self

    def dimensions(self, width: int, height: int) -> PositionBuilder:
        self._width = width
        self._height = height
        return self

    def build(self) -> Entity:
        if (
            self._animal_type is None
            or self._x is None
            or self._y is None
            or self._width is None
            or self._height is None
        ):
            raise ValueError("All builder fields must be provided with a value.")
        position = (
            Entity()
            .add_component(AnimalTypeComponent(self._animal_type))
            .add_component(PositionComponent(self._x, self._y))
        )
        return position


class SegmentBuilder(PositionBuilder):

    def build(self) -> Entity:
        segment = super().build()
        return segment


class CaveBuilder(PositionBuilder):

    def build(self) -> Entity:
        cave = super().build()
        return cave
