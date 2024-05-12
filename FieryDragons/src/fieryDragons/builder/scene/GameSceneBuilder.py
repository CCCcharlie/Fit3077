from __future__ import annotations

from engine.scene.Scene import Scene
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError

from fieryDragons.builder.entity.SegmentBuilder import SegmentBuilder
from fieryDragons.utils.AnimalType import AnimalType
from ...utils.CircleCoordinateIterator import CircleCoordinateIterator

class GameBuilder:

    def __init__(self, screen_width : int, screen_height : int):
        self.__screen_width = screen_width
        self.__screen_height = screen_height  
        self.__players : int | None = None
        self.__chit_cards : int | None = None
        self.__segments : int | None = None

    def setPlayers(self, players : int) -> GameBuilder:
        self.__players = players
        return self

    def setChitCards(self, chit_cards : int) -> GameBuilder:
        self.__chit_cards = chit_cards 
        return self

    def setSegments(self, segments : int) -> GameBuilder:
        self.__segments = segments
        return self

    def build(self) -> Scene:
        # Error handling 
        if self.__players is None: raise IncompleteBuilderError(self.__class__.__name__, "Players")
        if self.__chit_cards is None: raise IncompleteBuilderError(self.__class__.__name__, "Chit Cards")
        if self.__segments is None: raise IncompleteBuilderError(self.__class__.__name__, "Segements")

        # Build
        s = Scene()

        # Determine segment-related coordinates 
        center_x = self.__screen_width // 2
        center_y = self.__screen_height // 2

        # Place segments
        segment_iter = CircleCoordinateIterator(self.__segments, min(self.__screen_width, self.__screen_height) // 2, center_x, center_y, offset=1)
        for v2 in segment_iter:
            e = SegmentBuilder().setSize(segment_iter.size).setPosition(v2).setAnimalType(AnimalType.get_random_animal()).build()
            s.addEntity(e)

            # Place caves according to player count

        # Determine chit card-related coordinates

        # Place chit cards

        # Determine

        return s

