from selenium.webdriver.remote.webelement import WebElement
from data.locators import SignInPageLocators

from base.basepage import BasePage


class SignInPage(BasePage):

    def email_field_is_present(self) -> WebElement:
        return self.is_visible(SignInPageLocators.EMAIL_FIELD)

    def password_field_is_present(self) -> WebElement:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD)

    def password_field_is_present(self) -> WebElement:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD)

