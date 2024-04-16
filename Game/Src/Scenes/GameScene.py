from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType
from Game.Src.Objects.Cave import Cave
from Game.Src.Objects.ChitCard import ChitCard
from Game.Src.Objects.Player import Player
from Game.Src.Objects.Segment import Segment
from Game.Src.Objects.TurnManager import TurnManager
from Game.Src.Objects.VolcanoCard import VolcanoCard 


class GameScene(Scene):
  def __init__(self):
    super().__init__()

    #create player in scene
    player = Player()
    self.addEntity(player)
    TurnManager.PLAYER = player

    ## add the 8 volcano cards in the right position
    seg1 = Segment(10,10, AnimalType.BABY_DRAGON)
    seg2 = Segment(10,30, AnimalType.BAT)
    seg3 = Segment(10,50, AnimalType.SALAMANDER)

    seg1.get_component(PlayerPositionComponent).next = seg2.get_component(PlayerPositionComponent)
    seg2.get_component(PlayerPositionComponent).next = seg3.get_component(PlayerPositionComponent)

    # move player to seg 1
    ppc: PlayerPositionComponent = seg1.get_component(PlayerPositionComponent)
    ppc.addPlayer(player)

    # cave = Cave(10,100)
    segments = [seg1, seg2, seg3]

    volcCard = VolcanoCard(segments)
    self.addEntity(volcCard)



    # add the 16 chid cards in the centre
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
        chit_card = ChitCard(x_pos, y_pos, chit_card_radius)
        self.addEntity(chit_card)





