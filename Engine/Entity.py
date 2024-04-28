from abc import ABC, abstractmethod
from typing import List

# Import Component from the Engine module
from Engine import Component

# Entity class
class Entity(ABC): 
    def __init__(self):
        self.components: List[Component] = []

    def add_component(self, component: Component):
        # Check if the component is already added
        if component not in self.components:
            self.components.append(component)
        return component

    def get_component(self, component_type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def update(self):
        for component in self.components:
            component.update()

    def render(self, display_surf):
        for component in self.components:
            component.render(display_surf)


# Dragable class
class Dragable:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.dragging = False

    def update(self):
        # Update logic for dragable object
        pass

    def draw(self, screen):
        # Draw logic for dragable object
        pass


# Button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

    def update(self):
        # Update logic for button
        pass

    def draw(self, screen):
        # Draw logic for button
        pass
