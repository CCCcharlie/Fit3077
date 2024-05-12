from abc import ABC, abstractmethod

class Updateable(ABC):
  """
  Interface for objects that can be updated
  """
  @abstractmethod
  def update(self, dt: float):
    """
    Update the object by the provided delta time increment

    Args:
      dt (float): number of seconds this update must process
    """
    raise NotImplementedError()
