# Name Generator Microservice

## Communication Contract

This document outlines the contract for interacting with the Name Generator Microservice.

### Requesting Data from the Microservice

To request data from the Name Generator Microservice, make an HTTP POST request to the `/generate_names` endpoint.

#### Request Parameters

- **prompt**: (String) The text prompt given by the user to guide the name generation. It can be any descriptive word or phrase.
- **number_of_options**: (Integer) The number of name options the user wants.
- **name_type**: (String) The type of name to generate. Possible values are:
  - `male`
  - `female`
  - `unisex`
  - `random`

#### Example Request

Here’s an example using Python's `requests` library to make a POST request to the microservice:

```python
import requests

url = "http://localhost:5000/generate_names"
payload = {
    "prompt": "adventure",
    "number_of_options": 3,
    "name_type": "unisex"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### Receiving Data

The microservice responds with a JSON object containing the generated names and other information.

### Response Format

- **prompt**: (String) The text prompt used in the request.
- **number_of_options**: (Integer) The number of name options requested.
- **name_type**: (String) The type of name generated.
- **names**: (List) The list of names generated.

### Example Response

Here is an example of the JSON response from the microservice:

```JSON
{
    "prompt": "adventure",
    "number_of_options": 3,
    "name_type": "unisex",
    "names": ["Luxo", "Blami", "Veira"]
}
```

### Detailed Steps
#### 1. Make an HTTP POST Request:
- Use the specified endpoint and include the required parameters in the request body.
- Ensure the request headers include 'Content-Type: application/json'.
#### 2. Receive and Parse the JSON Response:
  - The response body will contain the generated names and other details in JSON format.
  - Parse the JSON response to extract and use the generated names as needed.

### Example Usage

Here is a complete example of how to request and receive data from the microservice:

```python
import requests

url = "http://localhost:5000/generate_names"
payload = {
    "prompt": "example prompt",
    "number_of_options": 3,
    "name_type": "unisex"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Prompt:", data["prompt"])
    print("Number of Options:", data["number_of_options"])
    print("Name Type:", data["name_type"])
    print("Names:", data["names"])
else:
    print("Failed to fetch data:", response.status_code, response.text)
```

## UML Sequence Diagram

![UML Diagram Microservice A](https://github.com/user-attachments/assets/194542a6-83b3-40ae-b45d-b4c28a5ca489)


