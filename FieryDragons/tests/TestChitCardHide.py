from engine.command.Command import Command
from engine.command.SetColorCommand import SetColorCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.CircleHitboxComponent import CircleHitboxComponent
from engine.component.hitbox.HitboxComponent import HitboxComponent
from engine.component.interaction.ButtonComponent import ButtonComponent
from engine.component.interaction.ClickableComponent import ClickableComponent
from engine.component.renderable.CircleComponent import CircleComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.ChitCard import ChitCard
from fieryDragons.command.ChitCardClickedCommand import ChitCardClickedCommand
from fieryDragons.enums.AnimalType import AnimalType
from pygame import Color


if __name__ == "__main__":
  world = World()
  scene = Scene()


  frontColor = AnimalType.BAT.get_colour()

  transformComponent: TransformComponent = TransformComponent()
  transformComponent.position = Vec2(100,100)

  hitbox: HitboxComponent = CircleHitboxComponent(transformComponent, 50, True)
  clickable: ClickableComponent = ClickableComponent(hitbox)

  front_circle = CircleComponent(transformComponent, 50, frontColor)
  front_circle.hide()
  back_circle = CircleComponent(transformComponent, 50, Color(0,0,0))

  ccComponent = ChitCard(front_circle, back_circle, AnimalType.BAT, 1)
  ccComponent.activateDebug()
  
  ccClickedCommand: Command = ChitCardClickedCommand(ccComponent)
  onDefault: Command = SetColorCommand(Color(0,0,0), back_circle)
  onHover: Command = SetColorCommand(Color(0,0,255), back_circle)
  onPressed: Command = SetColorCommand(Color(0,255,0), back_circle)



  button: ButtonComponent = ButtonComponent(clickable, ccClickedCommand, onDefault, onHover, onPressed)


  e = Entity()

  
  e.add_renderable(back_circle)
  e.add_renderable(front_circle)
  e.add_renderable(hitbox)

  e.add_updateable(clickable)
  e.add_updateable(button)
  e.add_updateable(ccComponent)



  scene.addEntity(e)
  world.setActiveScene(scene)
  world.start()