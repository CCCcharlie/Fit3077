from collections.abc import Sequence
from enum import Enum
from abc import ABC, abstractmethod
import pygame
from pygame import Rect, Surface
from pygame.color import Color
from ..Utils.settings import Settings
from .entity import Entity


class Component(ABC):

    parent: Entity

    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError()


class SurfaceComponent(Component):

    def __init__(self, surface: Surface) -> None:
        super().__init__()
        self.surface: Surface = surface

    def update(self) -> None:
        pos_component: PositionComponent = self.parent.get_components(
            PositionComponent
        )[0]
        pos = (pos_component.x, pos_component.y)
        Settings.get_instance().screen.blit(self.surface, pos)


class ImageComponent(SurfaceComponent):

    def __init__(self, image_path: str) -> None:
        super().__init__(pygame.image.load(image_path).convert())


class ToggleableComponent(Component):

    def __init__(self, component: Component) -> None:
        super().__init__()
        self.component = component
        self.active = True

    def update(self) -> None:
        if self.active:
            self.component.parent = self.parent
            self.component.update()


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
        else:
            raise ValueError("Provide dimensions or Rect object.")

    def update(self) -> None:
        pass


class ColouredRectangleComponent(RectangleComponent):

    def __init__(
        self,
        colour: Color,
        x: int | None = None,
        y: int | None = None,
        width: int | None = None,
        height: int | None = None,
        rect: Rect | None = None,
    ) -> None:
        super().__init__(x, y, width, height, rect)
        self.colour = colour

    def update(self) -> None:
        pygame.draw.rect(Settings.get_instance().screen, self.colour, self.rect)


class PositionComponent(Component):

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def update(self) -> None:
        pass


class SingleEntityComponent(Component):

    def __init__(self, relation_type: Enum, entity: Entity) -> None:
        self.entity = entity
        self.type = relation_type

    def update(self) -> None:
        if self.type is RelationType.CHILD:
            self.entity.update()


class MultiEntityComponent(Component):

    def __init__(self, relation_type: Enum, *entities: Entity) -> None:
        self.entities = [entity for entity in entities]
        self.type = relation_type

    def update(self) -> None:
        if self.type is RelationType.CHILD:
            for entity in self.entities:
                entity.update()


class RelationType(Enum):

    LINK = 0
    PARENT = 1
    CHILD = 2
    RELATION = 3
