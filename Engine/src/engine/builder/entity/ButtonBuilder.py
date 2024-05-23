from __future__ import annotations
from typing import List


from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.RectHitboxComponent import RectHitboxComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.utils.Vec2 import Vec2
from pygame import Color

from pygame.font import SysFont


from ...command.SetColorCommand import SetColorCommand
from ...command.Command import Command
from ...component.interaction.ButtonComponent import ButtonComponent
from ...component.interaction.ClickableComponent import ClickableComponent
from ...component.hitbox.HitboxComponent import HitboxComponent
from ...component.renderable.RenderableComponent import RenderableComponent
from ...exceptions.IncompleteBuilderError import IncompleteBuilderError
from ...entity.Entity import Entity

class ButtonBuilder:
  """
  Build a button
  """
  def __init__(self):
    """
    Initialise the builder
    """
    self.__renderable: RenderableComponent = None
    self.__hitbox: HitboxComponent = None

    self.__transformComponent = None
  
    self.__onClick: ClickableComponent = None

    self.__pressedColor: Color = Color(193, 18, 31)
    self.__hoverColor: Color = Color(102,155,188)
    self.__defaultColor: Color = Color(0,48,73)

    self.__position: Vec2 = None

    self.__text: str = None

    self.__storedRenderables: List[RenderableComponent] = []
    self.__rectDetails = None

  def setRectDetails(self, width: int, height: int) -> ButtonBuilder:
    self.__rectDetails = (width, height)
    return self


  def setText(self, text: str) -> ButtonBuilder:
    """
    Set the buttons text

    Args:
      text (str): The text of the button
    """
    self.__text = text
    return self

  def setHitbox(self, hitbox: HitboxComponent) -> ButtonBuilder:
    """
    Set the buttons hitbox

    Args:
      hitbox (HitboxComponent): The hitbox of the button
    """
    self.__hitbox = hitbox
    return self

  def setRenderableComponent(self, renderable: RenderableComponent) -> ButtonBuilder:
    """
    Set the buttons renderable 

    Args:
      renderable (RenderableComponent): The renderable of the button
    """
    self.__renderable = renderable
    return self

      
  def setOnClick(self, onClick: Command) -> ButtonBuilder:
    """
    Set the buttons onClick

    Args:
      onClick (Command): The command for onClick
    """
    self.__onClick = onClick
    return self

  def setPressedColor(self, pressedColor: Color) -> ButtonBuilder:
    """
    Set buttons pressed color
    
    Args:
      pressedColor (Color): The color when pressed
    """
    self.__pressedColor = pressedColor
    return self

  def setHoverColor(self, hoverColor: Color) -> ButtonBuilder:
    """
    Set buttons hover color
    
    Args:
      hoverColor (Color): The color when hover
    """
    self.__hoverColor = hoverColor
    return self

  def setDefaultColor(self, defaultColor: Color) -> ButtonBuilder:
    """
    Set buttons default color
    
    Args:
      defaultColor (Color): The color when default
    """
    self.__defaultColor = defaultColor
    return self

  def setPosition(self, position: Vec2) -> ButtonBuilder:
    """
    set the position of the button

    Args: 
      position (Vec2): The position of the button
    
    """ 
    self.__position = position
    return self
  
  def build(self) -> Entity:
    #checks
    if self.__hitbox is None and self.__renderable is not None:
      raise IncompleteBuilderError("Button","HitboxComponent")
    
    if self.__onClick is None:
      raise IncompleteBuilderError("Button", "OnClickCommand")
    
    if self.__rectDetails is None:
      self.__rectDetails = (100,50)

    # build
    e = Entity()



    if self.__renderable is None:
      if self.__position is None:
        raise IncompleteBuilderError("Button", "Position")
      self.__transformComponent = TransformComponent()
      self.__transformComponent.position = self.__position
      # create rectangle and hitbox   
      self.__renderable = RectComponent(self.__transformComponent, self.__rectDetails[0], self.__rectDetails[1], Color(0,0,0))
      self.__hitbox = RectHitboxComponent(self.__transformComponent, self.__rectDetails[0], self.__rectDetails[1], False)

    text = None
    if self.__text is not None:
      text = TextComponent(self.__transformComponent, self.__text, SysFont("Corbel", 60))

  
      

    defaultEvent = SetColorCommand(self.__defaultColor, self.__renderable)
    hoverEvent = SetColorCommand(self.__hoverColor, self.__renderable)
    pressedEvent = SetColorCommand(self.__pressedColor, self.__renderable)
    
    clickable = ClickableComponent(self.__hitbox)

    button = ButtonComponent(clickable, 
                             self.__onClick, 
                             defaultEvent, 
                             hoverEvent, 
                             pressedEvent)


    #now add to entity in the desired order 
    #renderables
    e.add_renderable(self.__renderable)
    e.add_renderable(self.__hitbox)
    if text is not None:
      e.add_renderable(text)

    #updateables
    e.add_updateable(clickable)
    e.add_updateable(button)

    self.__storedRenderables = [self.__renderable]
    if text is not None:
      self.__storedRenderables.append(text)  


    self.__renderable = None
    return e

  def getStoredRenderables(self) -> List[RenderableComponent]:
    return self.__storedRenderables
    