class IncompleteBuilderError(Exception):
  """
  Raised when a builder is incomplete and cannot be constructed
  """
  def __init__(self, builderName: str, requirementName: str):
    """
    Create the error of the form builder needs requirement

    Args:
      builderName (str): The name of the builder
      requirements (str): The name of the requirement
    """
    super().__init__(f"Builder is incomplete {builderName} needs {requirementName}")