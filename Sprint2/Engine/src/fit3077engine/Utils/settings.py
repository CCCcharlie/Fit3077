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

    def get_instance(self) -> Settings:
        if self.instance is None:
            self.instance = Settings(Scene())
        return self.instance
