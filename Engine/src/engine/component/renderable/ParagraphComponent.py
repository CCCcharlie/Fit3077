from collections.abc import Sequence
from typing import Tuple
from pygame.surface import Surface

from engine.utils.Vec2 import Vec2
from .TextComponent import TextComponent
from ..TransformComponent import TransformComponent
from pygame.font import Font
from pygame.color import Color


class ParagraphComponent(TextComponent):

    def __init__(
        self,
        transformComponent: TransformComponent,
        text: str,
        width: int,
        height: int,
        margin: float = 4,
        font: Font = None,
        color: Color = Color(255, 255, 255),
    ):
        self.__width = width
        self.__height = height
        self.__margin = margin
        self.__text_surfs : Sequence[Tuple[Surface, float]] = []
        super().__init__(transformComponent, text, font, color)

    def _generateImageSurface(self):
        self.__text_surfs = []
        lines = self._text.split("\n")
        currentHeight = 0
        for line in lines:
            words = line.split(" ")
            currentText = words.pop(0)

            # Render Line with potential breaks
            for word in words:
                newText = f"{currentText} {word}"
                textWidth, textHeight = self._font.size(newText)

                if currentHeight + textHeight > self.__height:
                    break

                if textWidth > self.__width:
                    self.__text_surfs.append((self._font.render(currentText, True, self._color), currentHeight))
                    _, textHeight = self._font.size(currentText)
                    currentText = word
                    currentHeight += textHeight + self.__margin
                else:
                    currentText = newText

            # Last Linebreak
            textWidth, textHeight = self._font.size(currentText)
            if currentHeight + textHeight <= self.__height: 
                self.__text_surfs.append((self._font.render(currentText, True, self._color), currentHeight))
                currentHeight += textHeight + self.__margin

    def render(self, display_surf: Surface) -> None:
        initialPos = self._transformComponent.position.clone()

        for surf, height in self.__text_surfs:
            self._transformComponent.position = initialPos + Vec2(0, height)
            self._setImageSurface(surf)
            super().render(display_surf)

        self._transformComponent.position = initialPos
