import time
from hospital import Hospital
from patient import Patient
from doctors import Doctor

hospital_name = input("Enter hospital name: ")
capacity = int(input("Enter maximum number of doctors: "))
hospital = Hospital(hospital_name, capacity)

while True:
  print(f"\n🏥 {hospital_name} System Menu")
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
    time.sleep(2)
  elif choice == "2":
    name = input("Patient name: ")
    age = int(input("Age: "))
    pid = input("ID: ")
    symptom = input("Symptom: ")
    priority = int(input("Priority (1-3): "))
    hospital.admit_patient(Patient(name, age, pid, symptom, priority))
    time.sleep(2)
  elif choice == "3":
    hospital.attend_next_patient()
    time.sleep(2)
  elif choice == "4":
    hospital.show_status()
    time.sleep(2)
  elif choice == "5":
    hospital.show_history()
    time.sleep(2)
  elif choice == "6":
    print("Goodbye!")
    break
  else:
    print("Invalid option.")
    time.sleep(2)
