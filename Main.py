from Engine import *
import pygame

if __name__ == "__main__":
  world = World()
  scene = Scene()
  world.setActiveScene(scene)

  scene.addEntity(Dragable(100,100,100,50,"TEST"))
  scene.addEntity(Button(300,100,100,50,"TEST", PrintCommand("button pressed")))


  # add animated test entity 
  e = Entity()
  trans = TransformComponent(e, 100, 200)
  anim = AnimatedComponent(e)
  click = ClickableComponent(e, 50,50)
  drag = DragComponent(e)

  e.add_component(trans)
  e.add_component(anim)
  e.add_component(click)
  e.add_component(drag)

  scene.addEntity(e)

  # start world up 
  world.gameLoop()
