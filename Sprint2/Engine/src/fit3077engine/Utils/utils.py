import pygame
from pygame.color import Color
from ..Events.handlers import PygameEventHandler

from ..ECS.scene import Scene
from .settings import Settings


def initialize(
    scene: Scene,
    screen_width: int = 1280,
    screen_height: int = 760,
    fps: int = 60,
    background_colour: Color = Color(255, 255, 255),
) -> Settings:
    pygame.init()
    return Settings(
        scene,
        screen_width=screen_width,
        screen_height=screen_height,
        fps=fps,
        background_colour=background_colour,
    )


def game_loop():
    settings = Settings.get_instance()

    while True:
        # Handle all Pygame Events
        for handler in PygameEventHandler.__subclasses__():
            handler.get_instance().handle_events()

        # Update Scene, Entities and Components
        settings.screen.fill(settings.background_colour)
        settings.scene.update()

        # Update Pygame display and wait for next frame
        pygame.display.update()
        settings.clock.tick(settings.fps)
