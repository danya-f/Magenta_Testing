from selenium.webdriver.remote.webelement import WebElement
from data.locators import SignInPageLocators
from data.locators import MyAccountPageLocators

from base.basepage import BasePage


class SignInPage(BasePage):

    def email_field(self) -> WebElement:
        return self.is_visible(SignInPageLocators.EMAIL_FIELD)

    def password_field(self) -> WebElement:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD)

    def signin_button(self) -> WebElement:
        return self.is_clickable(SignInPageLocators.SIGN_IN_BUTTON)

    def create_an_account_button(self) -> WebElement:
        return self.is_clickable(SignInPageLocators.CREATE_AN_ACCOUNT_FROM_SIGNIN_PAGE)

    def success_signin_msg(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.MY_ACCOUNT_MSG_THX_FOR_REGISTRATION)

    def error_signin_msg(self):
        return self.is_visible(SignInPageLocators.ERROR_SIGNIN_MSG)



