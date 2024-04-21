import pygame
from ..Events.handlers import PygameEventHandler

from ..ECS.scene import Scene
from .settings import Settings


def game_loop(
    scene: Scene, screen_width: int = 1280, screen_height: int = 760, fps: int = 60
):
    pygame.init()
    settings = Settings(scene, screen_width=screen_width, screen_height=screen_height)

    while True:
        # Handle all Pygame Events
        for handler in PygameEventHandler.__subclasses__():
            handler.handle_events()

        # Update Scene, Entities and Components
        settings.scene.update()

        # Update Pygame display and wait for next frame
        pygame.display.update()
        settings.clock.tick(fps)
