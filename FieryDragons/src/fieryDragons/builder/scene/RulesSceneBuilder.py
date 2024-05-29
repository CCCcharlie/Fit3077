from engine.builder.SceneBuilder import SceneBuilder
from engine.builder.entity.TextBuilder import TextBuilder
from engine.component.TransformComponent import TransformComponent, Vec2
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.component.renderable.ParagraphComponent import ParagraphComponent
from engine.scene.World import World
from pygame.color import Color


class RulesSceneBuilder(SceneBuilder):

    RULES = """Fiery Dragons is a board game focused on memorization.
Players start with a Dragon Token on one of the distinct caves around the board.
The aim of the game is to make a full rotation around the board and reach your home cave again.
Movement occurs by flipping Chit Cards in the center of the board. 
Depending on the result of the flip the Player will move a different number of spaces.

Good Luck and Have Fun!"""

    def build(self) -> Scene:
        scene = Scene()
        x = World().size[0] * 5/12

        # Header
        header = (
            TextBuilder()
            .setText("Rules")
            .setPosition(Vec2(x, World().size[1] * 1 / 16))
            .build()
        )
        scene.addEntity(header)

        # Paragraph
        e = Entity()
        transform = TransformComponent()
        transform.position = Vec2(x, World().size[1] * 1 / 8)
        paragraph = ParagraphComponent(transform, RulesSceneBuilder.RULES, 500, 500, color=Color(0,0,0))
        e.add_renderable(paragraph)
        scene.addEntity(e)

        return scene
