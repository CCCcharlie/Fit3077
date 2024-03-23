# --------------------- GENERATE TEST OBJECT ---------------------------------
# this would be a great usage of factories !!!! with some sort of world etc 
# create entities
from Engine import *


testEntity = Entity()

#create components
testEntity_transform = TransformComponent(testEntity, x=100, y=100)
testEntity_sprite = SpriteComponent(testEntity, image="Oven_connecting.png")

# add components to entity
testEntity.add_component(testEntity_transform)
testEntity.add_component(testEntity_sprite)

# add entity to world
# world.add_entity(testEntity)
