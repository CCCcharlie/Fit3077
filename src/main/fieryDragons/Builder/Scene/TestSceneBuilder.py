
from pygame import Color

from src.main.engine import * 



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