import csv


def read_data():
    patients = []

    file = open("patients.csv", "r")

    reader = csv.DictReader(file)

    for row in reader:
        patients.append(row)

    file.close()

    return patients


def display_records(patients):
    for patient in patients:
        print("ID:", patient["ID"])
        print("Age:", patient["Age"])
        print("BMI:", patient["BMI"])
        print("Blood Pressure:", patient["BloodPressure"])
        print("Glucose:", patient["Glucose"])
        print("Diabetes:", patient["Diabetes"])
        print("------------------------")


def count_cases(patients):
    positive = 0
    negative = 0

    for patient in patients:
        if patient["Diabetes"] == "Positive":
            positive += 1
        elif patient["Diabetes"] == "Negative":
            negative += 1

    print("Positive cases:", positive)
    print("Negative cases:", negative)


def find_high_glucose(patients):
    threshold = float(input("Enter glucose threshold: "))

    for patient in patients:
        glucose = float(patient["Glucose"])

        if glucose > threshold:
            print(patient)


def calculate_average_bmi(patients):
    total = 0

    for patient in patients:
        total = total + float(patient["BMI"])

    average = total / len(patients)

    print("Average BMI:", average)


def calculate_average_glucose(patients):
    total = 0

    for patient in patients:
        total = total + float(patient["Glucose"])

    average = total / len(patients)

    print("Average Glucose:", average)


def add_patient(patients):
    patient = {}

    patient["ID"] = input("Enter ID: ")
    patient["Age"] = input("Enter Age: ")
    patient["BMI"] = input("Enter BMI: ")
    patient["BloodPressure"] = input("Enter Blood Pressure: ")
    patient["Glucose"] = input("Enter Glucose: ")
    patient["Diabetes"] = input("Enter Diabetes prediction: ")

    patients.append(patient)


def update_patient(patients):
    patient_id = input("Enter ID to update: ")

    found = False

    for patient in patients:
        if patient["ID"] == patient_id:

            patient["Age"] = input("Enter new Age: ")
            patient["BMI"] = input("Enter new BMI: ")
            patient["BloodPressure"] = input("Enter new Blood Pressure: ")
            patient["Glucose"] = input("Enter new Glucose: ")
            patient["Diabetes"] = input("Enter new Diabetes prediction: ")

            found = True
            print("Patient updated.")
            break

    if found == False:
        print("Patient not found.")


def save_data(patients):
    file = open("patients.csv", "w", newline="")

    fieldnames = ["ID", "Age", "BMI", "BloodPressure", "Glucose", "Diabetes"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for patient in patients:
        writer.writerow(patient)

    file.close()


patients = read_data()

print("ALL PATIENT RECORDS")
display_records(patients)

print("DIABETES CASES")
count_cases(patients)

print("HIGH GLUCOSE PATIENTS")
find_high_glucose(patients)

print("AVERAGE BMI")
calculate_average_bmi(patients)

print("AVERAGE GLUCOSE")
calculate_average_glucose(patients)

print("ADD NEW PATIENT")
add_patient(patients)

print("UPDATE PATIENT")
update_patient(patients)

save_data(patients)

print("Data saved successfully.")