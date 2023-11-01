from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.element_to_be_clickable(locator))

    def current_url(self):
        return self.driver.current_url


