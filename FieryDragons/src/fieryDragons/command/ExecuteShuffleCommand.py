from engine.command.Command import Command
from typing import List, Tuple
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.Random import Random
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from fieryDragons.Player import Player


class ExecuteShuffleCommand(Command):
    """
    Shuffle the ChitCards by rearranging the order
    """
    def __init__(self, transforms: List[Tuple[TransformComponent, TransformComponent]]):
        self.__transforms = transforms

    def getNewTransforms(self, transforms: List[Tuple[TransformComponent, TransformComponent]]) -> List[Tuple[TransformComponent, TransformComponent]]:
        """
        Logic behind shuffling the card positions for the Shuffle Chit Card
        """
        newTransforms = [(t1.clone(), t2.clone()) for t1, t2 in transforms]
        Random().shuffle(newTransforms)
        return newTransforms
    
    def run(self):
        # get the new positions of each card
        newTransforms = self.getNewTransforms(self.__transforms)

        # calculate centre position
        centerPosition = Vec2(World().SCREEN_WIDTH//2, World().SCREEN_HEIGHT//2)
        centerTransform = TransformComponent()
        centerTransform.position = centerPosition


        #Move all cards to the centre
        for (t1, t2) in self.__transforms:
     
            moveToCenter1 = LinearMoveMFCommand(t1.clone(), centerTransform, t1, 250)
            moveToCenter2 = LinearMoveMFCommand(t2.clone(), centerTransform, t2, 250)

            MultiFrameCommandRunner().addCommand(moveToCenter1)
            MultiFrameCommandRunner().addCommand(moveToCenter2)

            moveToCenter1.run()
            moveToCenter2.run()

        
        #Then move all cards to their new positions
        for (t1, t2), (new_t1, new_t2) in zip(self.__transforms, newTransforms):
            moveToPosition1 = LinearMoveMFCommand(centerTransform, new_t1, t1, 250)
            moveToPosition2 = LinearMoveMFCommand(centerTransform, new_t2, t2, 250)

            delayMove1 = DelayExecuteMFMFCommand(moveToPosition1, 1000)
            delayMove2 = DelayExecuteMFMFCommand(moveToPosition2, 1000)

            MultiFrameCommandRunner().addCommand(delayMove1)
            MultiFrameCommandRunner().addCommand(delayMove2)

            delayMove1.run()
            delayMove2.run()

        #Position Hand sprites to fly in and then fly out
            

        #end the active players turn
        if Player.ACTIVE_PLAYER is not None:
            Player.ACTIVE_PLAYER.endTurn()
        PlayerTurnEndEmitter().notify()

        #update stored transforms to allow for a re-run
        self.__transforms = newTransforms
