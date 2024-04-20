import pygame
from ..ECS.components import ImageComponent, PositionComponent
from ..ECS.entity import Entity
from ..Events.handlers import PygameEventHandler

from ..ECS.scene import Scene
from .settings import Settings


def game_loop(screen_width: int = 1280, screen_height: int = 760, fps: int = 60):
    pygame.init()
    Settings.setup(screen_width=screen_width, screen_height=screen_height)
    ### TEMP
    scene = Scene()
    ent = Entity()
    ent.add_component(ImageComponent("./assets/test.png")).add_component(
        PositionComponent(30, 45)
    )
    scene.add_entity(ent)
    ### END TEMP
    Settings.update_scene(scene)

    while True:
        # Handle all Pygame Events
        for handler in PygameEventHandler.__subclasses__():
            handler.handle_events()

        # Update Scene, Entities and Components
        Settings.scene.update()

        # Update Pygame display and wait for next frame
        pygame.display.update()
        Settings.clock.tick(fps)
