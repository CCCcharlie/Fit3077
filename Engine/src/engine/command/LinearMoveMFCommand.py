
from engine.command.MultiFrameCommand import MultiFrameCommand
from engine.component.TransformComponent import TransformComponent

class LinearMoveMFCommand(MultiFrameCommand):
    """
    LinearMoveMFCommand class to linearly Move command
    """

    def __init__(self,
                 start: TransformComponent,
                 end: TransformComponent,
                 transform: TransformComponent,
                 totalTime: float):
        """
        Linear interpolation between two transform components

        Args:
          start (TransformComponent): The starting transform
          end (TransformComponent): The ending transform
          transform (TransformComponent): The transform to modify  
          totalTime (float): The total time given for the movement (in milliseconds)
        """

        self.__start: TransformComponent = start
        self.__end: TransformComponent = end
        self.__transform: TransformComponent = transform
        self.__totalTime: float = totalTime
        self.__timeElapsed: float = 0.0
        super().__init__()

    def update(self, dt: float):
        """
        Update of the linear movement
        """
        self.__timeElapsed += dt

        if self.__timeElapsed > self.__totalTime:
            # interpolation is done
            self._finish()
            self.__transform.copy(self.__end)
            return
        
        # calculate interpolation point
        s: float = self.__timeElapsed / self.__totalTime
        self.__transform.position = self.__start.position * (1 - s) + self.__end.position * s
        self.__transform.rotation = int(self.__start.rotation * (1 - s) + self.__end.rotation * s)
        self.__transform.scale = self.__start.scale * (1 - s) + self.__end.scale * s

 