from Engine import *
import pygame

if __name__ == "__main__":
  world = World()

  world.add_entity(Dragable(100,100,100,50,"TEST"))
  world.add_entity(Button(300,100,100,50,"TEST"))


  # add animated test entity 
  e = Entity()
  trans = TransformComponent(e, 100, 200)
  anim = AnimatedComponent(e)
  # to show how easy it is lets add the drag component 
  # should have a collider compoennt aswell 
  click = ClickableComponent(e, 50,50)
  drag = DragComponent(e)

  e.add_component(trans)
  e.add_component(anim)
  e.add_component(click)
  e.add_component(drag)

  world.add_entity(e)




  # start world up 
  world.gameLoop()
