from Engine import * 

class GameScene(Scene):
  def __init__(self):
    super().__init__()


    self.addEntity(Button(300,100,100,50,"Start", PrintCommand("button pressed")))
    self.addEntity(Button(300,100,100,50,"Quit", QuitCommand()))

