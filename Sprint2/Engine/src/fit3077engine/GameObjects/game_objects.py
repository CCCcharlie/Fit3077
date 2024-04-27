from abc import abstractmethod
from .interfaces import UpdateableInterface


class GameObject(UpdateableInterface):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update(self) -> None:
        pass
