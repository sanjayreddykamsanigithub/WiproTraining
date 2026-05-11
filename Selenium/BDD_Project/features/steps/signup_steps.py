import allure
from behave import given, when, then

from utils.logger import LogGen

from pages.signup_page import SignupPage

logger = LogGen.loggen()

@given(u'User Launches Demoblaze application')
def step_impl(context):
    logger.info('Demoblaze UPL loaded')

@when(u'User clicks on Sign up menu')
def step_impl(context):
    logger.info(  "Step: Click Sign Up Menu"  )
    context.signup_page = SignupPage(context.driver)
    context.signup_page.click_signup_menu()

@when(u'User enters signup username "{username}"')
def step_impl(context, username):
    logger.info(f"Step : Enter Username : {username}")
    context.signup_page.enter_username(username)

@when(u'User enters signup password "{password}"')
def step_impl(context, password):
    logger.info(f"Step : Enter password : {password}")
    context.signup_page.enter_password(password)

@when(u'User clicks Signup button')
logger.info(f"Step : Click Sign Up button")
    context.signup_page.click_signup_button()

@then(u'User should see signup success message')
def step_impl(context):
    logger.info("Step: Verify Successful. Sign Up Message")
    context.signup_page.verify_successful_sign_up()
    screenshot_path = (Screenshotutil.capture_screenshot(context.driver, screenshot_name: "successful signup"))
    logger.info("Screenshot Captured: (screenshot_path}")
    allure.attach(context.driver.get_screenshot_as_png(), name = "Successful Signup",
                  attachment_type=allure.attachment_type.PNG)
    assert alert_text == "Sign up successful.", 'sign up failed.'

def step_impl(context):