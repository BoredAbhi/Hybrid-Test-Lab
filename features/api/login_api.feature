Feature: Login API validation

  As an API client
  I want to validate the login endpoint
  So that I can ensure correct authentication behavior

  Scenario: Successful login with valid credentials
    Given the API endpoint "/api/login" is available
    When I send a POST request with valid username "standard_user" and password "secret_sauce"
    Then the response status code should be 200
    And the response should contain a token

  Scenario: Login fails with invalid credentials
    When I send a POST request with username "locked_out_user" and password "wrong_password"
    Then the response status code should be 401
    And the response should contain the message "Invalid credentials"

  Scenario: Login fails with missing username
    When I send a POST request with username "" and password "secret_sauce"
    Then the response status code should be 400
    And the response should contain the message "Username is required"

  Scenario: Login fails with missing password
    When I send a POST request with username "standard_user" and password ""
    Then the response status code should be 400
    And the response should contain the message "Password is required"
