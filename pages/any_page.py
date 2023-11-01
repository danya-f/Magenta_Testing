from selenium.webdriver.remote.webelement import WebElement
from data.locators import AnyPageLocators
from base.basepage import BasePage


class AnyPage(BasePage):

    def signin(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.SIGNIN_LINK)

    def create_account(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.CREATE_ACCOUNT_LINK)

    def search_items(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.SEARCH_FIELD)

    def cart(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.CART_LINK)

    # НИЖНИЙ КАТАЛОГ ССЫЛОК
    def search_terms(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.SEARCH_TERMS_LINK)

    def privacy_and_cookie_policy(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.PRIVACY_AND_COOKIE_POLICY_LINK)

    def advanced_search(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.ADVANCED_SEARCH_LINK)

    def orders_and_returns(self) -> WebElement:
        return self.is_clickable(AnyPageLocators.ORDERS_AND_RETURNS_LINK)
