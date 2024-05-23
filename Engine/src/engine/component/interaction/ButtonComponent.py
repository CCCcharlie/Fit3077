from ...command.Command import Command
from ...component.interaction.ClickableComponent import ClickableComponent
from ...entity.Updateable import Updateable


class ButtonComponent(Updateable):
  """
  Button class to handle button state logic.
  Pass it commands as needed to enact behaviours
  """
  def __init__(self, 
               clickableComponent: ClickableComponent, 
               onClick: Command, 
               onDefault: Command = None, 
               onHover: Command = None, 
               onPressed: Command = None):
    """
    Create the button passing on commands as needed.

    Pressed is when the button is hovered and clicked and clicked occurs 
    when the user lets go of the trigger button 

    Args:
      clickableComponent (ClickableComponent): The clickable to register button presses with
      onClick (Command): The logic for when the button is clicked (triggered on let go)
      onDefault (Command): The logic for when the button is deselected
      onHover (Command): The logic when the user hovers over the button
      onPressed (Command): The logic when the user presses (not triggers) the button 
    """


    self.__clickableComponent: ClickableComponent = clickableComponent
    self.__onClick: Command = onClick
    self.__onDefault: Command = onDefault
    self.__onHover: Command = onHover
    self.__onPressed: Command = onPressed


    # simple python state machine
    self.__switcher = {
      1: self.__defaultUpdate,
      2: self.__hoveredUpdate,
      3: self.__pressedUpdate,
    }

    self.__state = 1
    self.__onDefault.run()# run the default command to set the color 

  def __defaultUpdate(self):
    """
    The button is in its base state
    """
    if self.__clickableComponent.hover:
      self.__onHover.run()
      return 2 # is now hovering
    return 1    # is not hovering 
  
  def __hoveredUpdate(self):
    """
    Button is currently hovered
    """
    if self.__clickableComponent.hover:
      if self.__clickableComponent.clicked:
        self.__onPressed.run()
        return 3  # hover and clicked - > pressed
      return 2    # hover -> hover
    self.__onDefault.run()
    return 1      # hover -> normal
  
  def __pressedUpdate(self):
    """
    The button is being pressed
    """
    if self.__clickableComponent.hover:
      if self.__clickableComponent.clicked: 
        return 3 # pressed -> pressed
      self.__onClick.run()
      self.__onHover.run()
      return 2 # pressed -> hover
    self.__onDefault.run()
    return 1 # pressed -> default
  
  def __errorUpdate(self):
    """
    There was an error somewhere so we default back to state 1
    """
    print("Button had no state")
    self.__onDefault.run()
    return 1
  
  def update(self, dt: float):
    """
    Update the button
    """
    self.__state = self.__switcher.get(self.__state, self.__errorUpdate)()
  
