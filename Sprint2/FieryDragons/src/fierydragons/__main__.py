from fit3077engine.GameObjects.scenes import Scene
from fit3077engine.Utils.utils import game_loop, initialize

from fierydragons.GameObjects.game_objects import GameBoard


def main() -> None:
    # Init Scene
    scene = Scene()
    initialize(scene, "Fiery Dragons")

    # Run Game
    scene.add_object(GameBoard())
    game_loop()


if __name__ == "__main__":
    main()
