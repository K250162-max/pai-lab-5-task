import json

def read_file():
    file = open("model_results.json", "r")
    models = json.load(file)
    file.close()
    return models


def save_file(models):
    file = open("model_results.json", "w")
    json.dump(models, file, indent=4)
    file.close()


def display_best(models):
    highest_accuracy = models[0]
    highest_f1 = models[0]

    for model in models:
        if model["accuracy"] > highest_accuracy["accuracy"]:
            highest_accuracy = model

        if model["f1_score"] > highest_f1["f1_score"]:
            highest_f1 = model

    print("Highest Accuracy:")
    print(highest_accuracy)

    print("\nHighest F1-Score:")
    print(highest_f1)


def add_model(models):
    name = input("Enter model name: ")
    accuracy = float(input("Enter accuracy: "))
    precision = float(input("Enter precision: "))
    recall = float(input("Enter recall: "))
    f1_score = float(input("Enter F1-score: "))

    model = {
        "model_name": name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }

    models.append(model)
    save_file(models)


def update_model(models):
    name = input("Enter model name to update: ")

    for model in models:
        if model["model_name"] == name:
            model["accuracy"] = float(input("Enter new accuracy: "))
            model["precision"] = float(input("Enter new precision: "))
            model["recall"] = float(input("Enter new recall: "))
            model["f1_score"] = float(input("Enter new F1-score: "))

            save_file(models)
            print("Model updated successfully.")
            return

    print("Model not found.")


def remove_model(models):
    name = input("Enter model name to remove: ")

    for model in models:
        if model["model_name"] == name:
            models.remove(model)
            save_file(models)
            print("Model removed successfully.")
            return

    print("Model not found.")


def main():
    models = read_file()

    display_best(models)

    print("\n1. Add Model")
    print("2. Update Model")
    print("3. Remove Model")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_model(models)

    elif choice == "2":
        update_model(models)

    elif choice == "3":
        remove_model(models)

    else:
        print("Invalid choice.")


main()