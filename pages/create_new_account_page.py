from selenium.webdriver.remote.webelement import WebElement
from data.locators import CreateAnAccountPageLocators
from data.locators import MyAccountPageLocators
from base.basepage import BasePage


class CreateAnAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def first_name_field(self) -> WebElement:
        return self.is_visible(CreateAnAccountPageLocators.FIRST_NAME_FIELD)

    def first_name_fill(self, firstname) -> None:
        return self.is_visible(CreateAnAccountPageLocators.FIRST_NAME_FIELD).send_keys(firstname)

    def last_name_field(self) -> WebElement:
        return self.is_visible(CreateAnAccountPageLocators.LAST_NAME_FIELD)

    def last_name_fill(self, lastname) -> None:
        return self.is_visible(CreateAnAccountPageLocators.LAST_NAME_FIELD).send_keys(lastname)

    def email_field(self) -> WebElement:
        return self.is_visible(CreateAnAccountPageLocators.EMAIL_FIELD)

    def email_fill(self, email) -> None:
        return self.is_visible(CreateAnAccountPageLocators.EMAIL_FIELD).send_keys(email)

    def first_password_field(self) -> WebElement:
        return self.is_visible(CreateAnAccountPageLocators.PASSWORD_FIELD)

    def first_password_fill(self, password) -> None:
        return self.is_visible(CreateAnAccountPageLocators.PASSWORD_FIELD).send_keys(password)

    def confirm_password_field(self) -> WebElement:
        return self.is_visible(CreateAnAccountPageLocators.CONFIRM_PASSWORD_FIELD)

    def confirm_password_fill(self, password) -> None:
        return self.is_visible(CreateAnAccountPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

    def create_an_account_button_click(self) -> None:
        return self.is_clickable(CreateAnAccountPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def success_create_account_msg(self) -> str:
        return self.is_visible(MyAccountPageLocators.MY_ACCOUNT_MSG_THX_FOR_REGISTRATION).text

    def error_email_not_filled(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_EMAIL_FIELD).text

    def error_firstname_not_filled(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_FIRSTNAME_FIELD).text

    def error_lastname_not_filled(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_LASTNAME_FIELD).text

    def error_first_password_not_filled(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_FIRST_PASSWORD_FIELD).text

    def error_confirm_password_not_filled_or_not_same_like_first(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_CONFIRM_PASSWORD_FIELD).text

    def error_invalid_email(self):
        return self.is_visible(CreateAnAccountPageLocators.ERROR_EMAIL_FIELD).text

    def create_account_with_good_email_and_password(self, password, firstname, lastname, email):
        self.open()
        self.email_fill(email)
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_without_firstname(self, password, email, lastname):
        self.open()
        self.email_fill(email)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_without_lastname(self, password, email, firstname):
        self.open()
        self.email_fill(email)
        self.first_name_fill(firstname)
        self.first_password_fill(password)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_without_email(self, password, firstname, lastname):
        self.open()
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_without_second_password(self, email, password, firstname, lastname):
        self.open()
        self.email_fill(email)
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_without_first_password(self, email, password, firstname, lastname):
        self.open()
        self.email_fill(email)
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_with_invalid_email(self, password, firstname, lastname):
        self.open()
        self.email_fill('danyldykmail.com')
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.confirm_password_fill(password)
        self.create_an_account_button_click()
        return self

    def create_account_with_wrong_second_password(self, password, firstname, lastname, email):
        self.open()
        self.email_fill(email)
        self.first_name_fill(firstname)
        self.last_name_fill(lastname)
        self.first_password_fill(password)
        self.confirm_password_fill(password + '1')
        self.create_an_account_button_click()
        return self

    # def error_signin_msg(self):
    #     return self.is_visible(SignInPageLocators.ERROR_SIGNIN_MSG)
    #
    # def login_with_good_email_password(self ,page, email , password):
    #     self.open()
    #     self.email_field().send_keys(email)
    #     self.password_field().send_keys(password)
    #     self.signin_button().click()
    #     return page
    #
    # def login_with_fake_email_password(self ,page, email , password):
    #     self.open()
    #     self.email_field().send_keys(email)
    #     self.password_field().send_keys(password)
    #     self.signin_button().click()
    #     return page
