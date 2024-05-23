from abc import abstractmethod
from typing import Dict

class Serializable():
  """

  """
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

  