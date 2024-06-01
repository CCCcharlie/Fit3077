
import random
from engine.command.MultiFrameCommand import MultiFrameCommand
from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2

class ShakeMFCommand(MultiFrameCommand):
    """
    Shakes the transform by moving it to random positions
    """

    def __init__(self,
                 amount: int,
                 transform: TransformComponent,
                 totalTime: float):
        """
        Shake the transform component

        Args:
          amount (int): Shake amount
          transform (TransformComponent): The transform to modify  
          totalTime (float): The total time given for the movement (in milliseconds)
        """

        self.__amount = amount
        self.__transform: TransformComponent = transform
        self.__totalTime: float = totalTime

        self.__timeElapsed: float = 0.0
        self.__original: TransformComponent = self.__transform.clone()

        super().__init__()

    def update(self, dt: float):
        """
        Update method for the shake
        """
        self.__timeElapsed += dt

        if self.__timeElapsed > self.__totalTime:
            # interpolation is done
            self._finish()
            self.__transform.copy(self.__original)
            return
        
        # calculate the shake 
        offsetX = random.uniform(-self.__amount, self.__amount)
        offsetY = random.uniform(-self.__amount, self.__amount)

        self.__transform.position = Vec2(
            self.__original.position.x + offsetX,
            self.__original.position.y + offsetY
        )

    def run(self):
        super().run()
        self.__original = self.__transform.clone()


 