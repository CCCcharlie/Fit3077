#create circle of segments
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType


from engine.component.TransformComponent import TransformComponent


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
c_bby.setNext(seg1)

seg1.getNext().setCave(c_bat)
c_bat.setNext(seg1.getNext())

seg1.getNext().getNext().setCave(c_sal)
c_sal.setNext(seg1.getNext().getNext())

seg1.getNext().getNext().getNext().setCave(c_spi)
c_spi.setNext(seg1.getNext().getNext().getNext())

#make player
p = Player(c_bby)

#print out path
for el in p.path:
  print(el)



  

