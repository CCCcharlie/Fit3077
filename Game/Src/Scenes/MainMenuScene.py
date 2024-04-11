from Engine import * 
from Game.Src.Scenes.TestScene import TestScene

class MainMenuScene(Scene):
  def __init__(self):
    super().__init__()

    self.addEntity(Button(250,100,100,50,"Start", ChangeSceneCommand(TestScene())))
    self.addEntity(Button(250,200,100,50,"Quit", QuitCommand()))

