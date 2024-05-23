from typing import List
from engine.command.Command import Command
from engine.component.renderable.RenderableComponent import RenderableComponent


class ShowSavePopup(Command):
  def __init__(self, show: bool, popup: List[RenderableComponent], saveButton: List[RenderableComponent]):
    self.__popup = popup
    self.__saveButton = saveButton
    self.__show = show


  def extendPopop(self, p: List[RenderableComponent]):
    self.__popup.extend(p)

  def extendSave(self, p: List[RenderableComponent]):
    self.__saveButton.extend(p)

  def run(self):
    for r in self.__popup:
      if self.__show:
        r.show()
      else:
        r.hide()

    for r in self.__saveButton:
      if self.__show:
        r.hide()
      else:
        r.show()
   