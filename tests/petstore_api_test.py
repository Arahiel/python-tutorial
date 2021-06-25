import pytest
import requests
from jsonschema import validate

from tests import schemas


@pytest.mark.parametrize("status", [
    "available",
    "pending",
    "sold"
])
def test_get_pets_by_status_status_code_equals_200(status):
    response = requests.get(
        f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}")
    assert response.status_code == 200


@pytest.mark.parametrize("status", [
    "available",
    "pending",
    "sold"
])
def test_get_pets_by_status_json_schema_is_correct(status):
    response = requests.get(
        f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}")

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    resp_body = response.json()

    # Validate will raise exception if given json is not
    # what is described in schema.
    validate(instance=resp_body, schema=schemas.pet)
