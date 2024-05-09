from main.engine.utils.InterfaceMeta import InterfaceMeta

class Updateable(metaclass=InterfaceMeta):
  """
  Interface for objects that can be updated
  """
  def update(self, dt: float):
    """
    Update the object by the provided delta time increment

    Args:
      dt (float): number of seconds this update must process
    """
    raise NotImplementedError()
