
from pygame import Color

from src.main.engine.Scene import Scene
from src.main.engine.builder.entity.ButtonBuilder import ButtonBuilder
from src.main.engine.command.PrintCommand import PrintCommand
from src.main.engine.component.TransformComponent import TransformComponent
from src.main.engine.component.hitboxComponent.CircleHitboxComponent import CircleHitboxComponent
from src.main.engine.component.hitboxComponent.HitboxComponent import HitboxComponent
from src.main.engine.component.renderableComponent.RenderableComponent import RenderableComponent
from src.main.engine.component.renderableComponent.CircleComponent import CircleComponent
from src.main.engine.utils.Vec2 import Vec2





class TestSceneBuilder:
  def __init__(self):
    return
  
  def build(self) -> Scene:
    scene = Scene()

    buttonBuilder = ButtonBuilder()
    
    transform: TransformComponent = TransformComponent()
    transform.position = Vec2(10,10)
    hitbox: HitboxComponent = CircleHitboxComponent(transform, 10, True)
    renderable: RenderableComponent = CircleComponent(transform, 10, Color(0,0,0))

    buttonBuilder.setHitbox(hitbox)
    buttonBuilder.setRenderableComponent(renderable)

    buttonBuilder.setDefaultColor(Color(255,255,255))
    buttonBuilder.setHoverColor(Color(0,255,255))
    buttonBuilder.setPressedColor(Color(255,0,0))
    
    buttonBuilder.setOnClick(PrintCommand("Button Pressed"))

    e = buttonBuilder.build()
  
    scene.addEntity(e)

    return scene