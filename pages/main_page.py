from selenium.webdriver.remote.webelement import WebElement
from data.locators import MainPageLocators

from base.basepage import BasePage


class MainPage(BasePage):

    def signin_click(self) -> WebElement:
        return self.is_clickable(MainPageLocators.SIGNIN_LINK)

    def signin_click(self) -> WebElement:
        return self.is_clickable(MainPageLocators.SIGNIN_LINK)