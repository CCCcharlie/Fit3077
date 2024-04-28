from abc import ABC, abstractmethod
from .events import Event


class ObserverInterface(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def notify(self, event: Event) -> None:
        raise NotImplementedError()
