from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains

from data.locators import BasePageLocators


# from pages.any_page import AnyPage


class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        actions = ActionChains(self.driver)
        return actions.move_to_element(self.driver.find_element(*locator)).perform()

    # функция должна быть в пейдже где элемент ищем
    # def элемент(self) -> элемент:
    #     self.go_to_element(MainPageLocators.YELLOW_BUTTON_ORDER_PRESENTATION)
    #     return self.is_clickable(MainPageLocators.YELLOW_BUTTON_ORDER_PRESENTATION)

    def click_enter(self,locator):
        return locator.send_keys(Keys.ENTER)

    def current_url(self):
        return self.driver.current_url



    #УДАЛИЛ ЭНИ ПЕЙДЖ И ДОБАВИЛ В БЕЙЗПЕЙДЖ
    def signin_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.SIGNIN_LINK)

    def create_account_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.CREATE_ACCOUNT_LINK)

    def search_items_field(self) -> WebElement:
        return self.is_clickable(BasePageLocators.SEARCH_FIELD)

    def cart_icon_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.CART_LINK)

    # НИЖНИЙ КАТАЛОГ ССЫЛОК
    def search_terms_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.SEARCH_TERMS_LINK)

    def privacy_and_cookie_policy_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.PRIVACY_AND_COOKIE_POLICY_LINK)

    def advanced_search_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.ADVANCED_SEARCH_LINK)

    def orders_and_returns_link(self) -> WebElement:
        return self.is_clickable(BasePageLocators.ORDERS_AND_RETURNS_LINK)
    # УДАЛИЛ ЭНИ ПЕЙДЖ И ДОБАВИЛ В БЕЙЗПЕЙДЖ ДО СЮДА
