import pygame 

class Input(object):
  """
  Class used to track the input data 
  of the current gameloop iteration
  """

  quitflag = False
  mouse_visibility = True
  keys = {}

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
  def getmouseposition(this):
    """
    Returns the current position of the mouse
    """
    return pygame.mouse.get_pos()
  
  @classmethod
  def getmousebutton(this, index):
    """
    Returns weather a button of the mouse is pressed or not 

    Parameters
    ----------
    index : int 
      The index of the mouse button 
    """
    return pygame.mouse.get_pressed()[index]

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