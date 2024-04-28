from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
import pygame
from pygame import Rect, Surface
from ..Utils import settings
from .entity import Entity


class Component(ABC):

    entity: Entity = None

    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError()


class ImageComponent(Component):

    def __init__(self, image_path: str) -> None:
        super().__init__()
        self.surface: Surface = pygame.image.load(image_path).convert()

    def update(self) -> None:
        pos_component: PositionComponent = self.entity.get_component(PositionComponent)
        pos = (pos_component.x, pos_component.y)
        settings.Settings.screen.blit(self.surface, pos)


class RectangleComponent(Component):

    def __init__(
        self,
        x: int | None = None,
        y: int | None = None,
        width: int | None = None,
        height: int | None = None,
        rect: Rect | None = None,
    ) -> None:
        if rect is not None:
            self.rect: Rect = rect
        elif (
            x is not None and y is not None and width is not None and height is not None
        ):
            self.rect: Rect = Rect(x, y, width, height)

    def update(self) -> None:
        pass


class PositionComponent(Component):

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def update(self) -> None:
        pass
