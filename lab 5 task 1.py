
file = open("form.txt", "a")

file.write("101,rock,nrte,0.0055,12\n")
file.write("102,roc,nttrte,0.03,12\n")
file.write("103,pack,nrttte,0.02,12\n")

file.close()


def display():
    file = open("form.txt", "r")
    lines = file.readlines()

    for line in lines:
        print(line, end="")

    file.close()


def searchbyid(searchid):
    file = open("form.txt", "r")
    lines = file.readlines()

    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == searchid:
            print("ID:", data[0])
            print("Name:", data[1])
            print("Data set:", data[2])
            print("Learning rate:", data[3])
            print("Epochs:", data[4])
            found = True

    if found == False:
        print("Experiment not found")

    file.close()


def addexp():
    id = input("Enter ID: ")
    name = input("Enter name: ")
    dataset = input("Enter dataset: ")
    learningrate = input("Enter learning rate: ")
    epochs = input("Enter epochs: ")

    file = open("form.txt", "a")
    file.write(f"{id},{name},{dataset},{learningrate},{epochs}\n")
    file.close()

    print("Experiment added")


def updateexp():
    upid = input("Enter ID to update: ")
    name = input("Enter new name: ")
    dataset = input("Enter new dataset: ")
    learningrate = input("Enter new learning rate: ")
    epochs = input("Enter new epochs: ")

    file = open("form.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("form.txt", "w")
    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == upid:
            file.write(f"{upid},{name},{dataset},{learningrate},{epochs}\n")
            found = True
        else:
            file.write(line)

    file.close()

    if found:
        print("Experiment updated")
    else:
        print("Experiment not found")


def deleteexp():
    delid = input("Enter ID to delete: ")

    file = open("form.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("form.txt", "w")
    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == delid:
            found = True
            pass
        else:
            file.write(line)

    file.close()

    if found:
        print("Experiment deleted")
    else:
        print("Experiment not found")


while True:
    print("\n1. Display experiments")
    print("2. Search experiment")
    print("3. Add experiment")
    print("4. Update experiment")
    print("5. Delete experiment")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display()

    elif choice == "2":
        searchid = input("Enter ID to search: ")
        searchbyid(searchid)

    elif choice == "3":
        addexp()

    elif choice == "4":
        updateexp()

    elif choice == "5":
        deleteexp()

    elif choice == "6":
        break

    else:
        print("Invalid choice")