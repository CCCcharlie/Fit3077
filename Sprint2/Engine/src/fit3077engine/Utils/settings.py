from __future__ import annotations
import pygame

from ..ECS.scene import Scene


class Settings:

    instance: Settings | None = None

    def __init__(
        self, scene: Scene, *, screen_width: int = 1280, screen_height: int = 760
    ) -> None:
        if self.instance is not None:
            raise ValueError(
                "Cannot instantiate singleton Settings more than once. Use get_instance()"
            )
        self.instance = self
        self.scene = scene
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

    @classmethod
    def get_instance(cls) -> Settings:
        if cls.instance is None:
            cls.instance = Settings(Scene())
        return cls.instance
