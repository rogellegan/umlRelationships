# 4_association.py

class Doctor:
    def __init__(self, name: str):
        self.name = name

class Patient:
    def __init__(self, name: str):
        self.name = name

    def consult(self, doctor: Doctor):
        print(f"Patient {self.name} is consulting Doctor {doctor.name}.")

if __name__ == "__main__":
    doc = Doctor("Alice")
    patient = Patient("Bob")
    patient.consult(doc)
