import requests
import json


def get_prediction():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)

        print("GET Status Code:", response.status_code)
        print("GET Response:")
        print(response.json())

    except requests.exceptions.Timeout:
        print("GET request timed out.")

    except requests.exceptions.ConnectionError:
        print("GET connection error.")

    except ValueError:
        print("Invalid JSON response.")

    except requests.exceptions.RequestException:
        print("GET request failed.")


def create_prediction():

    url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        "image": "cat.jpg",
        "prediction": "Cat",
        "confidence": 0.95
    }

    try:
        response = requests.post(url, json=data, timeout=10)

        print("POST Status Code:", response.status_code)
        print("POST Response:")
        print(response.json())

    except requests.exceptions.Timeout:
        print("POST request timed out.")

    except requests.exceptions.ConnectionError:
        print("POST connection error.")

    except ValueError:
        print("Invalid JSON response.")

    except requests.exceptions.RequestException:
        print("POST request failed.")


def update_prediction():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    data = {
        "image": "cat.jpg",
        "prediction": "Dog",
        "confidence": 0.88
    }

    try:
        response = requests.put(url, json=data, timeout=10)

        print("PUT Status Code:", response.status_code)
        print("PUT Response:")
        print(response.json())

    except requests.exceptions.Timeout:
        print("PUT request timed out.")

    except requests.exceptions.ConnectionError:
        print("PUT connection error.")

    except ValueError:
        print("Invalid JSON response.")

    except requests.exceptions.RequestException:
        print("PUT request failed.")


def delete_prediction():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.delete(url, timeout=10)

        print("DELETE Status Code:", response.status_code)
        print("DELETE Response:")

        if response.text:
            print(response.json())
        else:
            print("Prediction deleted successfully.")

    except requests.exceptions.Timeout:
        print("DELETE request timed out.")

    except requests.exceptions.ConnectionError:
        print("DELETE connection error.")

    except ValueError:
        print("Invalid JSON response.")

    except requests.exceptions.RequestException:
        print("DELETE request failed.")


def main():

    get_prediction()

    print("--------------------")

    create_prediction()

    print("--------------------")

    update_prediction()

    print("--------------------")

    delete_prediction()


main()