from __future__ import annotations
from typing import Type
from pygame import Surface, display
import pygame

from ..Utils.scene import Scene


class Settings:

    screen: Surface = None
    clock: pygame.time.Clock = None
    scene: Scene = None

    def __init__(self) -> None:
        raise TypeError("Cannot instantiate a Settings object, instead use statically")

    @classmethod
    def setup(
        cls, *, screen_width: int = 1280, screen_height: int = 760, scene: Scene = None
    ) -> None:
        cls.screen = display.set_mode((screen_width, screen_height))
        cls.clock = pygame.time.Clock()
        cls.scene = scene if scene is not None else Scene()

    @classmethod
    def update_scene(cls, scene: Scene) -> Type["Settings"]:
        cls.scene = scene
        return cls
