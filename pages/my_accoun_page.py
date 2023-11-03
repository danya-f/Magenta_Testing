from base.basepage import BasePage
from selenium.webdriver.remote.webelement import WebElement
from data.locators import MyAccountPageLocators


class MyAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def my_account_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.MY_ACCOUNT_BUTTON)

    def my_orders_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.MY_ORDERS_BUTTON)

    def my_downloadable_products_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.MY_DOWNLOADABLE_PRODUCTS_BUTTON)

    def my_wish_list_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.MY_WISH_LIST_BUTTON)

    def address_book_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.ADDRESS_BOOK_BUTTON)

    def account_information_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.ACCOUNT_INFORMATION_BUTTON)

    def stored_payment_methods_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.STORED_PAYMENT_METHODS_BUTTON)

    def my_product_reviews_button(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.MY_PRODUCT_REVIEWS_BUTTON)
