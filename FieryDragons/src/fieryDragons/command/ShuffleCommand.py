from engine.command.Command import Command
from typing import List, Tuple
from engine.component.TransformComponent import TransformComponent
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from fieryDragons.Player import Player
from engine.entity.Updateable import Updateable
import random


class ShuffleCommand(Command, Updateable):
    """
        Shuffle the ChitCards by rearranging the order

        """
    def __init__(self, transforms: List[Tuple[TransformComponent, TransformComponent]]):
        self.__transforms = transforms
        self.__timer: float = -1

    def updateCardPositions(self):
        """
            Logic behind shuffling the card positions for the Shuffle Chit Card

            """
        current_positions = [(transform.position, transformComponent.position) for transform, transformComponent in self.__transforms]
        temp_positions = current_positions[:]
        random.shuffle(temp_positions)
        for (transform, transformComponent), (new_offset_position, new_position) in zip(self.__transforms, temp_positions):
            transform.position = new_offset_position
            transformComponent.position = new_position

    def run(self):
        if Player.ACTIVE_PLAYER is not None:
            Player.ACTIVE_PLAYER.endTurn()
        PlayerTurnEndEmitter().notify()


        self.__timer = 1000

    def update(self, dt: float):
        if self.__timer > 0:
            self.__timer -= dt
            if self.__timer < 0:
                self.__timer = -1
                self.updateCardPositions()
