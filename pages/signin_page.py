from selenium.webdriver.remote.webelement import WebElement
from data.locators import SignInPageLocators
from data.locators import MyAccountPageLocators
from base.basepage import BasePage
#ВРЕМЕННО ТЕСТИРУЮ
from pages.my_accoun_page import MyAccountPage



class SignInPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/login"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def email_field(self) -> WebElement:
        return self.is_visible(SignInPageLocators.EMAIL_FIELD)

    def email_field_fill(self, email) -> None:
        return self.is_visible(SignInPageLocators.EMAIL_FIELD).send_keys(email)

    def password_field(self) -> WebElement:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD)

    def password_field_fill(self, password) -> None:
        return self.is_visible(SignInPageLocators.PASSWORD_FIELD).send_keys(password)

    def signin_button(self) -> WebElement:
        return self.is_clickable(SignInPageLocators.SIGN_IN_BUTTON)

    def signin_button_click(self) -> None:
        return self.is_clickable(SignInPageLocators.SIGN_IN_BUTTON).click()

    def create_an_account_button(self) -> WebElement:
        return self.is_clickable(SignInPageLocators.CREATE_AN_ACCOUNT_FROM_SIGNIN_PAGE)

    def success_signin_msg(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.MY_ACCOUNT_MSG_THX_FOR_REGISTRATION)

    def error_signin_msg(self):
        return self.is_visible(SignInPageLocators.ERROR_SIGNIN_MSG)


    def login_with_good_email_password(self,email,password):
        self.open()
        self.email_field_fill(email)
        self.password_field_fill(password)
        self.signin_button().click()
        return MyAccountPage(driver=self.driver , url=self.driver.current_url)

    def login_with_fake_email_password(self, email, password):
        self.open()
        self.email_field().send_keys(email)
        self.password_field().send_keys(password)
        self.signin_button().click()
        return self

    def login_with_incorrect_password(self, email, password):
        self.open()
        self.email_field_fill(email)
        self.password_field_fill(password)
        self.signin_button().click()
        return self
