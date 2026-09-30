import requests
import json
import csv


def get_data(query):

    url = "https://jsonplaceholder.typicode.com/posts"

    params = {
        "userId": query
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if len(data) == 0:
                print("No data found.")
                return

            results = []

            for item in data:

                record = {
                    "text": item["body"],
                    "source": item["userId"],
                    "title": item["title"]
                }

                results.append(record)

                print("Text:", item["body"])
                print("Source:", item["userId"])
                print("Title:", item["title"])
                print("--------------------")

            try:

                with open("text_data.json", "w") as file:
                    json.dump(results, file, indent=4)

                print("Data saved to JSON file.")

                with open("text_data.csv", "w", newline="") as file:

                    fieldnames = ["text", "source", "title"]

                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()

                    for record in results:
                        writer.writerow(record)

                print("Data saved to CSV file.")

            except IOError:
                print("Error while saving the files.")

        else:
            print("Request failed. Status code:", response.status_code)

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet connection.")

    except ValueError:
        print("Invalid JSON response received.")

    except requests.exceptions.RequestException:
        print("An error occurred while requesting data.")


def main():

    query = input("Enter user ID to search: ")

    get_data(query)


main()