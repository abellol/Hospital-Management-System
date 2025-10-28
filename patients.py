import heapq
from patient import Patient

class PriorityQueue:
  def __init__(self):
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0

  def add_patient(self, patient:Patient, priority):
    """
    Adds a patient with a given priority to the queue.
    Lower numeric value means higher priority.
    """
    heapq.heappush(self.queue, (priority, patient))
    print(f"Patient {patient.name} added with priority {priority}.")

  def next_patient(self):
    """
    Retrieves and removes the patient with the highest priority.
    """
    if self.is_empty():
      print("No patients in queue.")
      return None
    priority, patient = heapq.heappop(self.queue)
    return patient

  def show_queue(self):
    """
    Displays all patients sorted by priority.
    """
    if self.is_empty():
      print("No patients in queue.")
      return
    print("Current patient queue (by priority):")
    for priority, patient in sorted(self.queue):
      print(f"  Priority {priority} -> {patient.show_info()}")
