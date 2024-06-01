from abc import abstractmethod
from typing import Dict

from engine.Random import Random

class Serializable():
  """

  """
  def __init__(self):

     self.__uuid: str = str(Random().getId())

  def getUUID(self) -> str:
     return self.__uuid
  
  @abstractmethod
  def serialise(self) -> Dict:
      """
      
      """
      raise NotImplementedError()
  
  @abstractmethod
  def deserialise(self, data: Dict) -> None:
     """
     """
     raise NotImplementedError()

  