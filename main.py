from hospital import Hospital
from patient import Patient
from doctors import Doctor

# Create a hospital with capacity for 5 doctors
hospital = Hospital("San Alejo", capacity=5)

# # Add doctors to the circular rotation
# hospital.register_doctor(Doctor("Smith"))
# hospital.register_doctor(Doctor("Lee"))
# hospital.register_doctor(Doctor("Brown"))
# hospital.register_doctor(Doctor("Davis"))
# hospital.register_doctor(Doctor("Taylor"))
# # Add some patients with different priorities
# hospital.admit_patient(Patient("Alice", 32, "P001", "Headache", priority=3))
# hospital.admit_patient(Patient("Bob", 45, "P002", "Chest pain", priority=1))
# hospital.admit_patient(Patient("Clara", 29, "P003", "Fracture", priority=2))
# hospital.admit_patient(Patient("David", 60, "P004", "High fever", priority=2))
# hospital.admit_patient(Patient("Eva", 50, "P005", "Shortness of breath", priority=1))

# # Display the current state
# hospital.show_status()

# # Attend patients
# print("\n--- Attending Patients ---")
# hospital.attend_next_patient()
# hospital.attend_next_patient()
# hospital.attend_next_patient()

# # Show updated status
# print("\n--- Updated Status ---")
# hospital.show_status()


hospital = Hospital("San Alejo", capacity=5)
while True:
  print("\n🏥 HOSPITAL SYSTEM MENU")
  print("1. Register Doctor")
  print("2. Admit Patient")
  print("3. Attend Next Patient")
  print("4. Show Status")
  print("5. Show history")
  print("6. Exit")
  choice = input("Select an option: ")
  if choice == "1":
    name = input("Enter doctor's name: ")
    hospital.register_doctor(Doctor(name))
  elif choice == "2":
    name = input("Patient name: ")
    age = int(input("Age: "))
    pid = input("ID: ")
    symptom = input("Symptom: ")
    priority = int(input("Priority (1-3): "))
    hospital.admit_patient(Patient(name, age, pid, symptom, priority))
  elif choice == "3":
    hospital.attend_next_patient()
  elif choice == "4":
    hospital.show_status()
  elif choice == "5":
    hospital.show_history()
  elif choice == "6":
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
