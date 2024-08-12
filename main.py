import requests
from jsonschema import validate, ValidationError
import pytest
expected_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }
}
def test_api_response():
    # Send GET request to the API endpoint
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Verify that the status code is 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Parse the JSON response after fetching the data.
    response_json = response.json()
    try:
        validate(instance=response_json, schema=expected_schema)
        print("Response is valid and contains the expected data structure.")
    except ValidationError as e:
        pytest.fail(f"Response is invalid: {e}")

if __name__ == '__main__':
    test_api_response()


