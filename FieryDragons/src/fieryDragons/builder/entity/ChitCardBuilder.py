from src.main.engine.command.SetColorCommand import SetColorCommand
from src.main.engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from src.main.engine.command.Command import Command
from fieryDragons.command.ChitCardClickedCommand import ChitCardClickedCommand
from fieryDragons.component.ChitCardComponent import ChitCardComponent
from src.main.engine import Vec2, Entity, ButtonComponent, CircleComponent, TransformComponent, ClickableComponent, HitboxComponent, CircleHitboxComponent
from pygame import Color

class ChitCardBuilder:
  """
  Build a chit card
  """
  def __init__(self, radius: int):
    """
    Create the builder 

    Args:
      radius (int): The radius of the chit card 
    """
    self.__position: Vec2 = Vec2(0,0)
    self.__radius = radius

    self.__frontColor = Color(255,255,255)
    self.__backColor = Color(0,0,0)

    self.__positionChanged = False

  def setPosition(self, position: Vec2):
    self.__positionChanged = True
    self.__position = position

  def build(self) -> Entity:
    if self.__positionChanged is False:
      raise IncompleteBuilderError("ChitCard", "Position")

    transformComponent: TransformComponent = TransformComponent()
    transformComponent.position = self.__position

    hitbox: HitboxComponent = CircleHitboxComponent(transformComponent, self.__radius, True)
    clickable: ClickableComponent = ClickableComponent(hitbox)

    front_circle = CircleComponent(transformComponent, self.__radius, self.__frontColor )
    back_circle = CircleComponent(transformComponent, self.__radius, self.__backColor)

    ccComponent = ChitCardComponent(front_circle, back_circle)
    
    ccClickedCommand: Command = ChitCardClickedCommand(ccComponent)
    onDefault: Command = SetColorCommand(Color(0,0,0), back_circle)
    onHover: Command = SetColorCommand(Color(0,0,255), back_circle)
    onPressed: Command = SetColorCommand(Color(0,255,0), back_circle)

    button: ButtonComponent = ButtonComponent(clickable, ccClickedCommand, onDefault, onHover, onPressed)


    e = Entity()

    e.add_renderable(front_circle)
    e.add_renderable(back_circle)
    e.add_renderable(hitbox)

    e.add_updateable(clickable)
    e.add_updateable(button)

    return e




