from Engine import *
from Game.Src.Objects.ChitCard import ChitCard 


class GameScene(Scene):
  def __init__(self):
    super().__init__()


    ## add the 8 volcano cards in the right position





    ## add the 16 chid cards in the centre
    # this is a square chit card generator
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





