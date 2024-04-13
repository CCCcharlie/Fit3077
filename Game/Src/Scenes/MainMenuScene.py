from Engine import * 
from Game.Src.Scenes.GameScene import GameScene

class MainMenuScene(Scene):
  def __init__(self):
    super().__init__()

    self.addEntity(Button(250,100,100,50,"Start", ChangeSceneCommand(GameScene())))
    self.addEntity(Button(250,200,100,50,"Quit", QuitCommand()))

