from abc import ABC, abstractmethod
from typing import Dict, List
import os

class FileDataHandler(ABC):
  def __init__(self):
    self._base_filename: str = "./saves/"
    if not os.path.exists(self._base_filename):
      os.makedirs(self._base_filename)

  @abstractmethod
  def save(self, saveId: int, data: Dict) -> None:
    """
    Save the current dictionary as save id

    Args:
      saveId (int): the id of the save
      data (Dict): The data to save
    
    """
    raise NotImplementedError()
    
  @abstractmethod
  def load(self, saveId: int) -> Dict:
    """
    Load the save file into a dict
    
    Args:
      saveId (int): the dave id to load
    """
    raise NotImplementedError()

  @abstractmethod
  def getAllSaves(self) -> List[int]:
    """
    Finds the index of available save files
    """
    raise NotImplementedError()

    