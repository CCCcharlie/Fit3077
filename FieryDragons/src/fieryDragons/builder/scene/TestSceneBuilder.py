
from engine.component.hitbox.HitboxComponent import HitboxComponent
from engine.component.renderable.RenderableComponent import RenderableComponent
from pygame import Color

from engine.scene.Scene import Scene
from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.CircleHitboxComponent import CircleHitboxComponent
from engine.component.renderable.CircleComponent import CircleComponent 
from engine.command.PrintCommand import PrintCommand

from engine import Entity, Renderable, Updateable # Exported from engine's __init__.py file
from engine.utils import Vec2 # Exported from engine.utils's __init__.py file

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
