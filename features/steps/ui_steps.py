from behave import given, when, then
from pages.login_page import LoginPage
from utils.browser_manager import BrowserManager

@given('the user is on the SauceDemo login page')
def step_open_login_page(context):
    context.driver = BrowserManager.get_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)

@then('the user should be redirected to the products page')
def step_verify_success_login(context):
    assert "inventory.html" in context.driver.current_url

@then('an error message "{expected_error}" should be displayed')
def step_verify_error_message(context, expected_error):
    error_text = context.login_page.get_error_message()
    assert expected_error in error_text
