from hospital import Hospital
from patient import Patient
from doctors import Doctor


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
