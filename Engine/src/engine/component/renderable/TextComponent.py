from pygame import Color
from pygame.font import Font, SysFont

from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent

class TextComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, text: str, font: Font = None, color: Color = Color(255,255,255)):
    """
    Text rendered
    Args:
      transformComponent (TransformComponent): The transform component the text is attached to 
      text (str): The message of the text
      font (Font): The font of the text
      color (Color): The color of the circle
    """
    self.__text: str = text
    if font is None:
      self.__font: Font = SysFont("Corbel", 30)
    else:
      self.__font: Font = font
    super().__init__(transformComponent)
    self.setColor(color)

  def setText(self, text: str):
    """
    Set the text
    
    Args:
      text (str): the content of the text
    """
    self.__text = text
    self._generateImageSurface()

  def setFont(self, font: Font):
    """
    Set the texts font
    
    Args:
      font (Font): The new font
    """
    self.__font = font
    self._generateImageSurface()

  def _generateImageSurface(self):
    """
    Generate text on the surface
    """
    textSurf = self.__font.render(self.__text, True, self._color)
    self._setImageSurface(textSurf)
