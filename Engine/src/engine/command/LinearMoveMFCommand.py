from MultiFrameCommand import MultiFrameCommand
from ...component.TransformComponent import TransformComponent
from ..utils.Vec2 import Vec2
from pygame import transform
class LinearMoveMFCommand(MultiFrameCommand):
    """
    LinearMoveMFCommand class to linearly Move command
    """

    def __init__(self,
                 startPos: Vec2,
                 endPos: Vec2,
                 transform: transform,
                 totalTime: float):
        """
        Create the movement based on the given time.

        Args:
          starPos (Vec2): The starting Position registered as a Vector2
          endPos (Vec2): The ending Position registered as a Vector2
          transform (Transform): The logic for when the button is deselected
          totalTime (Float): The total Time given for the movement
        """

        self.__startPos = startPos
        self.__endPos = endPos
        self.__transform = transform
        self.__totalTime = totalTime

    def update(self, dt: float):
        """
        Update of the linear movement
        """
        self.timeElapsed += dt
        if self.timeElapsed <= self.totalTime:
            t = self.timeElapsed / self.totalTime
            self.currentPos = self.startPos + (self.endPos - self.startPos) * t
            self.__transform.position(self.currentPos)
        else:
            self.currentPos = self.endPos

    def run(self):
        """
        Run the linear movement
        """
        return 1

    def finish(self):
        """
        Finish the linear movement
        """
        return 1