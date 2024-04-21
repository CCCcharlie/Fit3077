from fit3077engine.Utils import utils
from fit3077engine.ECS.scene import Scene
from fit3077engine.ECS.entity import Entity
from fit3077engine.ECS import components


def main() -> None:
    scene = Scene()
    utils.initialize(scene)

    img_comp = components.ImageComponent("./assets/test.png")
    ent = (
        Entity()
        .add_component(img_comp)
        .add_component(components.PositionComponent(0, 0))
        .add_component(components.RectangleComponent(rect=img_comp.surface.get_rect()))
    )
    scene.add_entity(ent)
    utils.game_loop()


if __name__ == "__main__":
    main()
