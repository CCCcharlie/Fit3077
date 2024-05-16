from engine.utils.Vec2 import Vec2
from pygame import Surface, Color, SRCALPHA, draw


from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent


class TrapezoidComponent(RenderableComponent):
  def __init__(self, transformComponent: TransformComponent, top: int, bottom: int, height: int, color: Color):
    """
    Create a Trapezoid

    Args:
      transformComponent (TransformComponent): The transform component the trapezoid is attached to 

      top (int): The length of the top 
      bottom (int): the length of the bottom (must be larger than top)
      height (int): The height of the trapezoid
      color (Color): The color of the rectangle
    """
    if bottom <= top:
       raise ValueError("Bottom must be greater than top")

    self.__top: int = top
    self.__bottom: int = bottom
    self.__height: int = height
    super().__init__(transformComponent)
    self.setColor(color)

  def _pivot(self) -> Vec2:
    return Vec2(+self.__bottom/2, 0)
  
  def _generateImageSurface(self) -> None:
    """
    Generate a trapezoid on an image surface
    """
    image_surf = Surface((self.__bottom + 1, self.__height +1), SRCALPHA)
    image_surf.fill((0, 0, 0, 0))  

    # Define vertices of the trapezoid
    offset = round((self.__bottom - self.__top) / 2)
    vertices = [
      (0,self.__height),##BL
      (self.__bottom,self.__height),##BR
      (offset + self.__top,0),##TR
      (offset,0),##TL
      # (0,self.__height),##BL
    ]

    # Draw lines to connect the vertices
    draw.polygon(image_surf, self._color, vertices)

    # draw.aalines(image_surf, self., True, vertices)
    self._setImageSurface(image_surf)
 
