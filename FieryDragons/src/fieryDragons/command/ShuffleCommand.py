from engine.command.Command import Command
from typing import Dict, List, Tuple
from engine.command.DelayExecuteMFCommand import DelayExecuteMFCommand
from engine.component.TransformComponent import TransformComponent
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from fieryDragons.command.ExecuteShuffleCommand import ExecuteShuffleCommand



class ShuffleCommand(Command):
    """
    Shuffle the ChitCards by rearranging the order
    """
    def __init__(self, transforms: List[Tuple[TransformComponent, TransformComponent]], leftHand: TransformComponent):
        self.__transforms: List[Tuple[TransformComponent, TransformComponent]] = transforms
        self.__leftHand: TransformComponent = leftHand

    def run(self):
        command = DelayExecuteMFCommand(ExecuteShuffleCommand(self.__transforms, self.__leftHand), 1000)
        MultiFrameCommandRunner().addCommand(command)
        command.run()

        
