from engine.command.Command import Command
from typing import List, Tuple
from engine.component.TransformComponent import TransformComponent
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from fieryDragons.Player import Player

import random



class ShuffleCommand(Command):
    def __init__(self, transforms: List[Tuple[TransformComponent, TransformComponent]]):
        self.__transforms = transforms

    def updateCardPositions(self):
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
        self.updateCardPositions()
