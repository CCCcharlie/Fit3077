from fit3077engine.Utils import utils
from fit3077engine.ECS.scene import Scene
from fit3077engine.ECS.entity import Entity
from fit3077engine.ECS import components
from .EntityBuilders.builders import GameBoardBuilder


def main() -> None:
    # Setup Scene
    scene = Scene()
    utils.initialize(scene)
    board = GameBoardBuilder().build()
    scene.add_entity(board)

    # Run Game
    utils.game_loop()


if __name__ == "__main__":
    main()
