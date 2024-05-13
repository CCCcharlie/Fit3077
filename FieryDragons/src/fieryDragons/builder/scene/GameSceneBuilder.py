from __future__ import annotations

from engine.scene.Scene import Scene
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from engine.utils.Vec2 import Vec2
from fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.utils.GridCoordinateIterator import GridCoordinateIterator
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator


class GameSceneBuilder:
    def __init__(self, screen_width: int, screen_height: int):
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__players: int | None = None
        self.__chit_cards: int | None = None
        self.__segments: int | None = None

    def setPlayers(self, players: int) -> GameSceneBuilder:
        self.__players = players
        return self

    def setChitCards(self, chit_cards: int) -> GameSceneBuilder:
        self.__chit_cards = chit_cards
        return self

    def setSegments(self, segments: int) -> GameSceneBuilder:
        self.__segments = segments
        return self

    def build(self) -> Scene:
        # Error handling
        if self.__players is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Players")
        if self.__chit_cards is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Chit Cards")
        if self.__segments is None:
            raise IncompleteBuilderError(self.__class__.__name__, "Segements")

        # Build
        s = Scene()

        # Determine segment-related coordinates
        center_x = self.__screen_width // 2
        center_y = self.__screen_height // 2

        # Place segments
        segment_iter = CircleCoordinateIterator(
            self.__segments,
            5 * min(self.__screen_width, self.__screen_height) // 8,
            center_x,
            center_y,
            offset=1,
        )
        for t in segment_iter:
            e = (
                SegmentBuilder()
                .setSize(segment_iter.size)
                .setTransform(t)
                .setAnimalType(AnimalType.get_random_animal())
                .build()
            )
            s.addEntity(e)

            # Place caves according to player count

        # Place chit cards
        gridIterator = GridCoordinateIterator(
            4,
            4,
            Vec2(center_x, center_y),
            min(self.__screen_width, self.__screen_height) // 2,
            min(self.__screen_width, self.__screen_height) // 2,
        )
        chitCardBuilder = ChitCardBuilder(40)
        chitCardBuilder.setAnimalType(AnimalType.BABY_DRAGON)
        chitCardBuilder.setAmount(1)

        for v2 in gridIterator:
            e = chitCardBuilder.setPosition(v2).build()
            # s.addEntity(e)

        # Determine

        return s
