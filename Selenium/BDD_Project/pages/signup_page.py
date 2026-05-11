import allure
import self
from utils.logger import  LogGen
from utils.waits import Waitutils, WaitUtils

from utils.screenshot_util import ScreenshotUtil

from utils import logger

from locators.signup_locators import SignupLocators

Logger = LogGen.Loggen ()

class SignupPage:
    def _init_(self, driver):
        self.driver = driver

    def click_signup_menu(self):
        logger.info("Clicking Sign Up Menu")
        WaitUtils.wait_for_element_clickable(self.driver, SignupLocators.SIGNUP_MENU ).click()

    def enter_username(self, username):
        logger.info(f"Entering Username : {username}")
        element = WaitUtils.wait_for_element_visible(  self.driver, SignupLocators.USERNAME_INPUT  )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering Password")
        element = WaitUtils.wait_for_element_visible( self.driver, SignupPageLocators.PASSWORD_INPUT )
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        logger.info("Clicking Login Button")
        WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.LOGIN_BUTTON
        ).click()

    def click_signup_button(self): 1
        logger.info("Clicking Sign up Button")
        WaitUtils.wait_for_element_clickable(  self.driver, SignupLocators.SIGNUP_BUTTON  ).click()

    def verify_successful_signup(self):
        logger.info("Verifying SignUp Alert")
        alert = Waitutils.wait_for_alert(  self.driver    )
        alert.text = alert.text
        logger.info(  f"Alert Message : {alert_text}"   )
        ScreenshotUtil.capture_screenshot(self.driver, "signup_alert"
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Signup Alert Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        alert.accept()
        return alert_text