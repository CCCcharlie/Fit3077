from Engine import *
import pygame

if __name__ == "__main__":
  world = World()

  # --------------------- GENERATE TEST OBJECT ---------------------------------
  # this would be a great usage of factories !!!! with some sort of world etc 
  # create entities
  e = Entity()

  e_trans = TransformComponent(e, x=100, y=100)
  e_rect = RectComponent(e, 100, 50, (0,0,250))
  e_text = TextComponent(e, "TEST", pygame.font.SysFont("Corbel", 30), (250,250,250))
  e_clickable = ClickableComponent(e, 100, 50)


  e.add_component(e_trans)
  e.add_component(e_rect)
  e.add_component(e_text)
  e.add_component(e_clickable)

  # add entity to world
  world.add_entity(e)
  world.add_entity(Button(300,100,100,50,"TEST"))

  # start world up 
  world.gameLoop()
