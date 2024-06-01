from engine.utils.Vec2 import Vec2
from pygame import Surface, Color, SRCALPHA, draw
import math

from ...component.renderable.RenderableComponent import RenderableComponent
from ...component.TransformComponent import TransformComponent


class CircularSegmentTrapezoidComponent(RenderableComponent):
    def __init__(self, transformComponent: TransformComponent, height: int, inner_radius: float, angle: int, color: Color):
        """
        Create a Circular Segment Trapezoid

        Args:
            transformComponent (TransformComponent): The transform component the trapezoid is attached to 
            height (int): The height of the trapezoid
            color (Color): The color of the trapezoid
            radius (float): The radius of the arcs
            angle (int): The angle (in degrees) that the arc sweeps out
        """
        self.__height: int = height
        self.__inner_radius: float = inner_radius
        self.__outer_radius: float = inner_radius + height
        self.__angle: int = angle
        self.__pivot = Vec2(0,0)
        super().__init__(transformComponent)
        self.setColor(color)

    def _pivot(self) -> Vec2:
        return self.__pivot
    
    def _generateImageSurface(self) -> None:
        """
        Generate a circular segment trapezoid on an image surface
        """
        # Sweep out top arc
        top_arc = []
        for angle in range(90 - (self.__angle // 2), 90 + (self.__angle // 2) + 1):
            radian = math.radians(angle)
            x = self.__outer_radius * math.cos(radian)
            y = self.__outer_radius * math.sin(radian)
            top_arc.append((x, y))

        # Sweep out bottom arc
        bottom_arc = []
        for angle in range(90 - (self.__angle // 2), 90 + (self.__angle // 2) + 1):
            radian = math.radians(angle)
            x = self.__inner_radius * math.cos(radian)
            y = self.__inner_radius * math.sin(radian)
            bottom_arc.append((x, y))

        # Populate vertices in the right order
        vertices = []
        vertices.extend(top_arc)
        vertices.extend(reversed(bottom_arc))

        # from vertices generate bounding box 
        min_x, min_y = vertices[0]
        max_x, max_y = vertices[0]
        for x, y in vertices:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

        # apply offset so that the mins are now (0,0)
        adjustedVertices = [(x - min_x, y - min_y) for x, y in vertices]
        max_x -= min_x
        max_y -= min_y

        # draw image
        width = max_x
        height = max_y
        image_surf = Surface((width, height), SRCALPHA)
        image_surf.fill((0, 0, 0, 0))

        # Draw the filled polygon using the vertices
        draw.polygon(image_surf, self._color, adjustedVertices)

        # draw a circle at the middle of the polygon
        a1 = math.radians(90 - (self.__angle // 2))
        y1 = self.__inner_radius * math.sin(a1)
        a2 = math.radians(90)
        y2 = self.__inner_radius * math.sin(a2)
        self.__pivot = Vec2(width/2, y2 - y1)
        
        draw.circle(image_surf, Color(0,255,0), (self.__pivot.x, self.__pivot.y),5)
        # draw.circle(image_surf, Color(0,255,0), (0,0),5)
        # draw.circle(image_surf, Color(255,0,0), (width,0),5)
        # draw.circle(image_surf, Color(0,0,255), (0, height),5)
        # draw.circle(image_surf, Color(255,0,0), (width, height),5)

        self._setImageSurface(image_surf)
