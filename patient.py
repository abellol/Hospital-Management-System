class Patient:
  """
  Represents a patient in the hospital management system.
  Stores personal details, medical information, and current treatment status.
  """

  def __init__(self, name, age, identification, symptom, priority, status="Waiting"):
    if age < 0:
      raise ValueError("Age must be a positive number.")
    if priority not in range(1, 4):
      raise ValueError("Priority must be between 1 (highest) and 3 (lowest).")

    self.name = name
    self.age = age
    self.id = identification
    self.symptom = symptom
    self.priority = priority
    self.status = status

  def __lt__(self, other:"Patient"):
    return self.priority < other.priority
  
  def show_info(self):
    """Return a formatted string with patient details."""
    return (
      f"Patient: {self.name}\n"
      f"  Age: {self.age}\n"
      f"  ID: {self.id}\n"
      f"  Symptom: {self.symptom}\n"
      f"  Priority: {self.priority}\n"
      f"  Status: {self.status}"
    )

  def __str__(self):
    """Readable string representation of the patient."""
    return f"[{self.priority}] {self.name} ({self.status}) - {self.symptom}"

  def update_status(self, new_status):
    self.status = new_status
  def mark_as_treated(self):
    """Set the patient status to 'Treated'."""
    self.status = "Treated"

