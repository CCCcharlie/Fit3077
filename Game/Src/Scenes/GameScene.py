from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType
from Game.Src.Enums.ChitCardType import ChitCardType
from Game.Src.Objects.Cave import Cave
from Game.Src.Objects.ChitCard import ChitCard
from Game.Src.Objects.Player import Player
from Game.Src.Objects.Segment import Segment
from Game.Src.Objects.TurnManager import TurnManager
from Game.Src.Objects.VolcanoCard import VolcanoCard 

import random

class RectangleCoordinateGenerator():
  def __init__(self):
    # setup generator variables
    self.startX = 40
    self.startY = 20
    self.rectWidth = World.SCREEN_WIDTH - 80
    self.rectHeight = World.SCREEN_HEIGHT - 4

    self.numRows = 9
    self.numColumns = 9

  def generateCoordinates(self, row, column):
    x = self.startX + self.rectWidth * row / (self.numRows + 1)
    y = self.startY + self.rectHeight * column/ (self.numRows + 1)
    return (x,y)

class GridPositionGenerator():
  def __init__(self):
    self.rcg = RectangleCoordinateGenerator()
    self.positions = [
      [(1,2), (1,3), (1,4), (0,3)],
      [(1,5), (1,6), (1,7), (0,6)],
      [(2,8), (3,8), (4,8), (3,9)],
      [(5,8), (6,8), (7,8), (6,9)],
      [(8,7), (8,6), (8,5), (9,6)],
      [(8,4), (8,3), (8,2), (9,3)],
      [(7,1), (6,1), (5,1), (6,0)],
      [(4,1), (3,1), (2,1), (3,0)]
    ]
  def getCoords(self, volcanoIndex, segmentIndex):
    row, column = self.positions[volcanoIndex][segmentIndex]
    return self.rcg.generateCoordinates(row, column)

class GameScene(Scene):
  def __init__(self):
    super().__init__()

    #create gridPositionGenerator
    gpg = GridPositionGenerator()

    #create player in scene
    player = Player()
    TurnManager.PLAYER = player

    ## define volcano cards
    volcanoCardSpecifications = [
      ([AnimalType.BABY_DRAGON, AnimalType.BAT, AnimalType.SPIDER],True),
      ([AnimalType.SALAMANDER, AnimalType.SPIDER, AnimalType.BAT],True),
      ([AnimalType.SPIDER, AnimalType.SALAMANDER, AnimalType.BABY_DRAGON],True),
      ([AnimalType.BAT, AnimalType.SPIDER, AnimalType.BABY_DRAGON],True),
      ([AnimalType.SPIDER, AnimalType.BAT, AnimalType.SALAMANDER],False),
      ([AnimalType.BABY_DRAGON, AnimalType.SALAMANDER, AnimalType.BAT],False),
      ([AnimalType.BAT, AnimalType.BABY_DRAGON, AnimalType.SALAMANDER],False),
      ([AnimalType.SALAMANDER, AnimalType.BABY_DRAGON, AnimalType.SPIDER],False)
    ]

    # define cave types
    caves = [
      AnimalType.BABY_DRAGON,
      AnimalType.SALAMANDER,
      AnimalType.BAT,
      AnimalType.SPIDER,
    ]

    # randomise
    random.shuffle(volcanoCardSpecifications)
    random.shuffle(caves)

    previousLastSegment: PlayerPositionComponent = None
    firstElementCreated: PlayerPositionComponent = None

    for i, (animals, hasCave) in enumerate(volcanoCardSpecifications):
      x, y = gpg.getCoords(i, 0)
      seg1 = Segment(x, y, animals[0])
      x, y = gpg.getCoords(i, 1)
      seg2 = Segment(x, y, animals[1])
      x, y = gpg.getCoords(i, 2)
      seg3 = Segment(x, y, animals[2])

      pp_seg1: PlayerPositionComponent = seg1.get_component(PlayerPositionComponent)
      pp_seg2: PlayerPositionComponent = seg2.get_component(PlayerPositionComponent)
      pp_seg3: PlayerPositionComponent = seg3.get_component(PlayerPositionComponent)
                                  
      cave = None
      if hasCave:
        caveAnimal = caves.pop()
        x, y = gpg.getCoords(i, 3)
        cave = Cave(x, y, caveAnimal)

      # link components
      if previousLastSegment is not None:
        previousLastSegment.setNext(pp_seg1)
      pp_seg1.setNext(pp_seg2)
      pp_seg2.setNext(pp_seg3)
    
      pp_seg1.setPrevious(previousLastSegment)
      pp_seg2.setPrevious(pp_seg1)
      pp_seg3.setPrevious(pp_seg2)

      if cave:
        pp_seg2.setCave(cave)
    
      segments = [seg1, seg2, seg3]

      volcCard = VolcanoCard(segments, cave)
      self.addEntity(volcCard)

      


      #grab the first element created 
      if i == 0:
        firstElementCreated = pp_seg1

      #set the previous last element 
      previousLastSegment = pp_seg3
    
    # add player to scene
    self.addEntity(player)

    # link the front and back
    firstElementCreated.setPrevious(previousLastSegment)
    previousLastSegment.setPrevious(firstElementCreated)

    print("adding player to")
    print(firstElementCreated)
    firstElementCreated.addPlayer(player)

    chitCards = [
      (1, ChitCardType.SALAMANDER),
      (2, ChitCardType.SALAMANDER),
      (3, ChitCardType.SALAMANDER),
      (1, ChitCardType.BAT),
      (2, ChitCardType.BAT),
      (3, ChitCardType.BAT),
      (1, ChitCardType.SPIDER),
      (2, ChitCardType.SPIDER),
      (3, ChitCardType.SPIDER),
      (1, ChitCardType.BABY_DRAGON),
      (2, ChitCardType.BABY_DRAGON),
      (3, ChitCardType.BABY_DRAGON),
      (1, ChitCardType.PIRATE_DRAGON),
      (1, ChitCardType.PIRATE_DRAGON),
      (2, ChitCardType.PIRATE_DRAGON),
      (2, ChitCardType.PIRATE_DRAGON)
    ]

    random.shuffle(chitCards)

    #this is a square chit card generator
    start_pos_x = 3 * World().SCREEN_WIDTH/8
    end_pos_x = 5 * World().SCREEN_WIDTH/8
    start_pos_y = World().SCREEN_HEIGHT/4
    end_pos_y = 3 * World().SCREEN_HEIGHT/4

    #apply correction factor for width and height
    chit_card_radius = 10
    start_pos_x = start_pos_x + chit_card_radius
    start_pos_y = start_pos_y + chit_card_radius
    end_pos_x = end_pos_x - chit_card_radius
    end_pos_y = end_pos_y - chit_card_radius

    num_chit_x = 4
    num_chit_y = 4

    x_interval = (end_pos_x - start_pos_x) / (num_chit_x - 1)
    y_interval = (end_pos_y - start_pos_y) / (num_chit_y - 1)

    for i in range(num_chit_x):
      for j in range(num_chit_y):
        x_pos = start_pos_x + i * x_interval
        y_pos = start_pos_y + j * y_interval

        # create chit card at x and y position
        count, type = chitCards.pop()
        chit_card = ChitCard(x_pos, y_pos, chit_card_radius, type, count)
        self.addEntity(chit_card)

  
