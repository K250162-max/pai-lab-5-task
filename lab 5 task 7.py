import requests
import json
import csv


def get_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    params = {
        "userId": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.ConnectionError:
        print("API connection error.")

    except requests.exceptions.Timeout:
        print("API request timed out.")

    except requests.exceptions.HTTPError:
        print("HTTP error:", response.status_code)

    except ValueError:
        print("Invalid JSON data received.")

    else:
        print("Data received successfully.")

        results = []

        for item in data:
            record = {
                "id": item["id"],
                "userId": item["userId"],
                "title": item["title"],
                "text": item["body"]
            }

            results.append(record)

        return results

    finally:
        print("API request completed.")


def analyze_data(data):

    if data is None:
        return

    total = 0

    for item in data:
        total = total + item["id"]

    average = total / len(data)

    highest = data[0]

    for item in data:
        if item["id"] > highest["id"]:
            highest = item

    print("\nAnalysis")
    print("Number of records:", len(data))
    print("Average ID:", average)
    print("Highest ID:", highest["id"])
    print("Title of highest ID:", highest["title"])


def save_files(data):

    try:

        with open("processed_data.json", "w") as file:
            json.dump(data, file, indent=4)

        with open("processed_data.csv", "w", newline="") as file:

            fieldnames = ["id", "userId", "title", "text"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for item in data:
                writer.writerow(item)

        print("\nData saved successfully.")

    except IOError:
        print("Error while saving files.")


def read_files():

    try:

        with open("processed_data.json", "r") as file:
            json_data = json.load(file)

        print("\nJSON file verified.")
        print(json_data)

    except FileNotFoundError:
        print("JSON file not found.")

    except ValueError:
        print("JSON file contains invalid data.")

    try:

        with open("processed_data.csv", "r") as file:

            reader = csv.DictReader(file)

            print("\nCSV file verified.")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("CSV file not found.")

    finally:
        print("\nFile reading completed.")


def main():

    data = get_data()

    if data is not None:

        analyze_data(data)

        save_files(data)

        read_files()


main()