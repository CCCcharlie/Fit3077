from __future__ import annotations
import pygame
from pygame.color import Color

from ..GameObjects.scenes import Scene


class Settings:

    instance: Settings | None = None

    def __init__(
        self,
        scene: Scene,
        title: str,
        *,
        screen_width: int = 1280,
        screen_height: int = 760,
        fps: int = 60,
        background_colour: Color = Color(255, 255, 255),
    ) -> None:
        if self.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {Settings.__name__} more than once. Use get_instance()"
            )
        self.scene = scene
        self.title = title
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background_colour = background_colour
        Settings.instance = self

    @classmethod
    def get_instance(cls) -> Settings:
        if cls.instance is None:
            raise ValueError("Instantiate once using constructor first.")
        return cls.instance
