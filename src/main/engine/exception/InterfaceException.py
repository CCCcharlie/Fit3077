class InterfaceException(Exception):
  """"
  Exception raised when a method of an interface is not implemented in a concrete class.
  """
  def __init__(self, className: str, method: str):
    """
    Initialize the InterfaceException instance.

    Args:
      className (str): The name of the class where the method is missing.
      method (str): The name of the method that is not implemented. 
    """
    self.message = f"Interface Exception: {className}.{method} not implemented."
    super().__init__(self.message)