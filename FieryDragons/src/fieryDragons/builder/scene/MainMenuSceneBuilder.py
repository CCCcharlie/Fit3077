from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.scene.Scene import Scene
from engine.utils.Vec2 import Vec2


class MainMenuSceneBuilder:
  def build() -> Scene:
    s = Scene() 

    bb = ButtonBuilder()

    # add start button
    bb.setPosition = Vec2(250,100)
    

    # add start button
    # self.addEntity(Button(250,100,100,50,"Start", ChangeSceneCommand(GameScene())))
    

    # add quit button
    #self.addEntity(Button(250,200,100,50,"Quit", QuitCommand()))

    
    

    return s 
    
  


  

