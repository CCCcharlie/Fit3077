from pygame import Color

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
  
    self.__onClick: ClickableComponent = None

    self.__pressedColor: Color = None
    self.__hoverColor: Color = None
    self.__defaultColor: Color = None



  def setHitbox(self, hitbox: HitboxComponent):
    """
    Set the buttons hitbox

    Args:
      hitbox (HitboxComponent): The hitbox of the button
    """
    self.__hitbox = hitbox

  def setRenderableComponent(self, renderable: RenderableComponent):
    """
    Set the buttons renderable 

    Args:
      renderable (RenderableComponent): The renderable of the button
    """
    self.__renderable = renderable

      
  def setOnClick(self, onClick: Command):
    """
    Set the buttons onClick

    Args:
      onClick (Command): The command for onClick
    """
    self.__onClick = onClick

  def setPressedColor(self, pressedColor: Color):
    """
    Set buttons pressed color
    
    Args:
      pressedColor (Color): The color when pressed
    """
    self.__pressedColor = pressedColor

  def setHoverColor(self, hoverColor: Color):
    """
    Set buttons hover color
    
    Args:
      hoverColor (Color): The color when hover
    """
    self.__hoverColor = hoverColor

  def setDefaultColor(self, defaultColor: Color):
    """
    Set buttons default color
    
    Args:
      defaultColor (Color): The color when default
    """
    self.__defaultColor = defaultColor
    
    
    
  
  def build(self) -> Entity:
    #checks
    if self.__hitbox is None:
      raise IncompleteBuilderError("Button","HitboxComponent")
    
    if self.__renderable is None:
      raise IncompleteBuilderError("Button", "RenderableComponent")
    
    if self.__onClick is None:
      raise IncompleteBuilderError("Button", "OnClickCommand")


    # todo set this to optional either pressed color or event !!
    if self.__pressedColor is None:
      raise IncompleteBuilderError("Button", "PressedColor")
    
    if self.__hoverColor is None:
      raise IncompleteBuilderError("Button", "HoverColor")
    
    if self.__defaultColor is None:
      raise IncompleteBuilderError("Button", "DefaultColor")

    # build
    e = Entity()

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

    #updateables
    e.add_updateable(clickable)
    e.add_updateable(button)
    
    return e