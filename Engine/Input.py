import pygame 

class Input(object):
  """
  Class used to track the input data 
  of the current gameloop iteration
  """

  quitflag = False
  mouse_visibility = True
  keys = {}
  mouse_buttons = {}

  @classmethod
  def update(this):
    """
    updates class information using the input event data 
    """

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        this.quitflag = True
      
      if event.type == pygame.KEYUP:
        this.keys[event.key] = False

      if event.type == pygame.KEYDOWN:
        this.keys[event.key] = True

      if event.type == pygame.MOUSEBUTTONDOWN:
        this.mouse_buttons[event.button] = True

      if event.type == pygame.MOUSEBUTTONUP:
        this.mouse_buttons[event.button] = False



  @classmethod
  def getkey(this, key):
    """
    Returns weather a key is pressed or not 

    Parameters
    ----------
    key: int
      Pygame key constant
    """
    try:
      return this.keys[key]
    except KeyError:
      # key has never been pressed
      this.keys[key] = False
      return False
    
  @classmethod
  def getMouseButton(this, button: int):
    """
    Returns weather a button is pressed or not 

    Parameters
    ----------
    button: int
      Pygame button constant
    """
    try:
      return this.mouse_buttons[button]
    except KeyError:
      # key has never been pressed
      this.mouse_buttons[button] = False
      return False
    
  @classmethod 
  def getmouseposition(this):
    """
    Returns the current position of the mouse
    """
    return pygame.mouse.get_pos()
  
  @classmethod
  def getmousevisibility(this):
    """
    Returns a boolean indicating whether the mouse is visible or not
    """
    return this.mouse_visibility 
    
  @classmethod
  def setmousevisibility(this, boolean):
    """
    Sets the visibility of the mouse

    Parameters
    ----------
    boolean : bool
    """
    this.mouse_visibility = boolean
    pygame.mouse.set_visible(boolean)