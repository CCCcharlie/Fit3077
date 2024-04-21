from __future__ import annotations
import pygame

from ..ECS.scene import Scene


class Settings:

    instance: Settings | None = None

    def __init__(
        self,
        scene: Scene,
        *,
        screen_width: int = 1280,
        screen_height: int = 760,
        fps: int = 60,
    ) -> None:
        if self.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {Settings.__name__} more than once. Use get_instance()"
            )
        self.scene = scene
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.fps = fps
        self.clock = pygame.time.Clock()
        Settings.instance = self

    @classmethod
    def get_instance(cls) -> Settings:
        if cls.instance is None:
            cls.instance = Settings(Scene())
        return cls.instance
