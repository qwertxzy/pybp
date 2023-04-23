class Action:
  """
  Defines one action that is contained in the execution plan.
  """
  def __init__(self, command, path, status = "PLANNED"):
    self.command = command
    self.path = path
    self.status = status
