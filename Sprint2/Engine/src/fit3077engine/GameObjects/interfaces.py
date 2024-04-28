from abc import ABC, abstractmethod


class UpdateableInterface(ABC):

    @abstractmethod
    def update(self) -> None:
        pass


class RenderableInterface(ABC):

    @abstractmethod
    def render(self) -> None:
        pass
