class Hospital:
    def __init__(self, patient_id, name, disease):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease

    def __str__(self):
        return f"Patient ID: {self.patient_id}\nName: {self.name}\nDisease: {self.disease}"

p1 = Hospital(201, "Amit", "Fever")
print(p1)