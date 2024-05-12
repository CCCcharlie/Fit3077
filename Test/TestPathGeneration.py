## build out say segments with 4 types of caves
from src.main.fieryDragons.Player import Player
from src.main.engine.component.TransformComponent import TransformComponent
from src.main.fieryDragons.Segment import Segment
from src.main.fieryDragons.enums.AnimalType import AnimalType


#create circle of segments
tc1 = TransformComponent()
seg1= Segment(tc1, AnimalType.BAT)
previous = seg1
for i in range(20):
  tc = TransformComponent()
  seg = Segment(tc, AnimalType.SALAMANDER)
  previous.setNext(seg)
  previous = seg
previous.setNext(seg1)


#create caves
c_bby = Segment(tc1, AnimalType.BABY_DRAGON)
c_bat = Segment(tc1, AnimalType.BAT)
c_sal = Segment(tc1, AnimalType.SALAMANDER)
c_spi = Segment(tc1, AnimalType.SPIDER)

 
# add caves
seg1.setCave(c_bby)
seg1.getNext().setCave(c_bat)
seg1.getNext().getNext().setCave(c_sal)
seg1.getNext().getNext().getNext().setCave(c_spi)

#make player
p = Player(c_bby)

#print out path
for el in p.path:
  print(el)



  

