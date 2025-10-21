class Doctor:
  """
  Represents a doctor in the hospital system.
  """

  def __init__(self, name):
    self.name = name
    self.disponible = True

  def show_info(self):
    return f"[Dr. {self.name}] - {'Available' if self.disponible else 'Busy'}"

  def occupy(self):
    """Mark doctor as busy while treating a patient."""
    self.disponible = False

  def release(self):
    """Mark doctor as available after finishing a consultation."""
    self.disponible = True

