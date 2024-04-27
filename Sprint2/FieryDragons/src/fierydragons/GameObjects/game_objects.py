from __future__ import annotations
from abc import abstractmethod
from fit3077engine.GameObjects.game_objects import GameObject
from fit3077engine.GameObjects.interfaces import RenderableInterface
from fit3077engine.Events.observer import ObserverInterface
from fit3077engine.Events.events import Event


class GameBoard(GameObject, ObserverInterface):

    instance: GameBoard | None = None

    def __init__(self) -> None:
        if self.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {GameBoard.__name__} more than once. Use get_instance()"
            )
        super().__init__()

    @classmethod
    def get_instance(cls) -> GameBoard:
        if cls.instance is None:
            cls.instance = GameBoard()
        return cls.instance

    def update(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass


class Player(GameObject, RenderableInterface, ObserverInterface):

    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass


class GamePosition(GameObject, RenderableInterface):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def next(self, player: Player) -> GamePosition:
        pass

    def update(self) -> None:
        return super().update()

    def render(self) -> None:
        pass


class SegmentPosition(GamePosition):

    def __init__(self) -> None:
        super().__init__()

    def next(self, player: Player) -> GamePosition:
        return super().next(player)


class CavePosition(GamePosition):

    def __init__(self) -> None:
        super().__init__()

    def next(self, player: Player) -> GamePosition:
        return super().next(player)

    def render(self) -> None:
        return super().render()


class ChitCard(GameObject, RenderableInterface, ObserverInterface):

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        pass

    def notify(self, event: Event) -> None:
        pass
