from behave import given, when, then
import requests

API_BASE_URL = "http://localhost:5000"  # or wherever your test API runs

@given('the API endpoint "{endpoint}" is available')
def step_set_endpoint(context, endpoint):
    context.endpoint = API_BASE_URL + endpoint

@when('I send a POST request with valid username "{username}" and password "{password}"')
@when('I send a POST request with username "{username}" and password "{password}"')
def step_send_login_request(context, username, password):
    payload = {"username": username, "password": password}
    context.response = requests.post(context.endpoint, json=payload)

@then('the response status code should be {expected_status:d}')
def step_check_status_code(context, expected_status):
    assert context.response.status_code == expected_status

@then('the response should contain a token')
def step_check_token_in_response(context):
    assert "token" in context.response.json()

@then('the response should contain the message "{expected_message}"')
def step_check_error_message(context, expected_message):
    assert expected_message in context.response.json().get("message", "")
