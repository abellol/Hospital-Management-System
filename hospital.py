from patient import Patient
from doctor import Doctor
from doctors import CircularQueue
from patients import PriorityQueue
import time

class Hospital:
  """
  Represents a hospital management system.
  
  It coordinates the rotation of available doctors (CircularQueue)
  and manages patient care based on urgency (PriorityQueue).
  """

  def __init__(self, name, capacity):
    """
    Initialize the hospital system.

    Args:
      name (str): Name of the hospital.
      doctor_queue (CircularQueue): Queue managing doctor rotation.
      patient_queue (PriorityQueue): Queue managing patients by priority.
      self.history: "Dynamic Array" to save all patients history 
    """
    self.name = name
    self.doctor_queue = CircularQueue(capacity)
    self.patient_queue = PriorityQueue()
    self.history = []

  def register_doctor(self, doctor:Doctor):
    """Add a doctor to the rotation schedule."""
    self.doctor_queue.add_doctor(doctor)

  def admit_patient(self, patient:Patient):
    """Add a patient to the waiting list according to their priority."""
    self.patient_queue.add_patient(patient, patient.priority)

  def attend_next_patient(self):
    """
    Assigns the next available doctor to the highest-priority patient.
    The doctor attends the patient for 3 seconds and then becomes available again.
    """
    if self.patient_queue.is_empty():
      print("No patients waiting for treatment.")
      return
    if self.doctor_queue.is_empty():
      print("No doctors available to attend patients.")
      return

    doctor: Doctor = self.doctor_queue.next_doctor()
    patient: Patient = self.patient_queue.next_patient()

    doctor.occupy()
    patient.update_status("Being Treated")

    print(f"\n Doctor {doctor.name} is now attending patient {patient.name}...")
    print(f"Patient condition: {patient.symptom}")
    time.sleep(3)  # Simulate treatment time

    # Finish treatment
    doctor.release()
    patient.mark_as_treated()
    print(f"Doctor {doctor.name} has finished treating {patient.name}.\n")

    self.doctor_queue.rotate_doctor(doctor)
    self.history.append((doctor.name, patient.name, patient.symptom))

  def show_status(self):
    """Display the current hospital status: doctors and patients."""
    print(f"\nHospital: {self.name}")
    self.doctor_queue.show_doctors()
    self.patient_queue.show_queue()
    

  def show_history(self):
    """Displays all previous treatments."""
    print("\n===== Treatment History =====")
    if not self.history:
      print("No treatments have been recorded yet.")
      return
    for i, (doctor, patient, symptom) in enumerate(self.history, start=1):
      print(f"{i}. Dr. {doctor} treated {patient} (Symptom: {symptom})")
    print("=============================\n")
