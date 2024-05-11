from src.main.engine.utils.Vec2 import Vec2
from src.main.engine.Input import Input
from src.main.engine import Updateable
from src.main.engine.component.hitboxComponent.HitboxComponent import HitboxComponent


class ClickableComponent(Updateable):
  """
  Clickable component
  
  Access the hover and click interface to extract values 
  """
  def __init__(self, hitboxComponent: HitboxComponent):
    """
    Create the clickable component
    
    Args:
      hitboxComponent (HitboxComponent): The hitbox to check mouse over with
    """
    self.__hitboxComponent = hitboxComponent

    self.__hover: bool = False
    self.__clicked: bool = False

  def update(self, dt: float):
    """
    Update the clicked and hover variables
    """
    x,y = Input().getmouseposition()
    self.__hover = self.__hitboxComponent.checkPointCollision(Vec2(x,y))

    if(self.__hover):
      self.__clicked = Input().getMouseButton(1)
    else:
      if self.__clicked:
        self.__clicked = Input().getMouseButton(1)



  @property
  def clicked(self) -> bool:
    """
    Is the clickable currently clicked
    """
    return self.__clicked
  
  @property 
  def hover(self) -> bool:
    """
    Is the clickable currently hovered
    """
    return self.__hover
    
    