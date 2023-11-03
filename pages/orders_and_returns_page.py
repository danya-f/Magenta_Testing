from selenium.webdriver.remote.webelement import WebElement
from data.locators import OrdersAndReturnsPageLocators
from base.basepage import BasePage


class OrdersAndReturnsPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/sales/guest/form/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def order_id_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD)

    def error_order_id_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD_MESSAGE_ERROR)


    def billing_lastname_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD)

    def error_billing_lastname_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD_MESSAGE_ERROR)

    def find_order_by_dropdown(self) -> WebElement:
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_DROPDOWN)

    def email_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD)

    def error_email_not_filled_or_incorrect_type(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD_MESSAGE_ERROR)

    def billing_zip_code_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ZIP_FIELD)

    def error_billing_zip_code_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ZIP_FIELD_MESSAGE_ERROR)

    def continue_button(self):
        return self.is_clickable(OrdersAndReturnsPageLocators.CONTINUE_BUTTON)

    def select_find_order_by_zip_code_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_ZIP_CODE_DROPDOWN).click()

    def label_billing_zip_code(self):
        return self.is_visible(OrdersAndReturnsPageLocators.LABEL_ZIP_FIELD)

    def select_find_order_by_email_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_EMAIL_DROPDOWN).click()

    def label_email(self):
        return self.is_visible(OrdersAndReturnsPageLocators.LABEL_EMAIL_FIELD)


