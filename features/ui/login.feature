Feature: Login functionality for SauceDemo

  As a user of SauceDemo
  I want to be able to log in with valid credentials
  So that I can access the products page

  Background:
    Given the user is on the SauceDemo login page

  Scenario: Successful login with valid credentials
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the products page

  Scenario: Login fails with invalid credentials
    When the user logs in with username "locked_out_user" and password "wrong_password"
    Then an error message "Epic sadface: Username and password do not match any user in this service" should be displayed

  Scenario: Login fails with missing username
    When the user logs in with username "" and password "secret_sauce"
    Then an error message "Epic sadface: Username is required" should be displayed

  Scenario: Login fails with missing password
    When the user logs in with username "standard_user" and password ""
    Then an error message "Epic sadface: Password is required" should be displayed
