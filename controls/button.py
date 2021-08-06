from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Button:

    def __init__(self, driver, locator=None):
        super().__init__(driver)
        self._locator = locator

    def click_button(self, locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()

