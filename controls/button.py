from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Button:

    def __init__(self, driver, by=By.CSS_SELECTOR, selector=None):
        self._locator = (by, selector)
        self.driver = driver

    def click(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self._locator))
        self.driver.find_element(*self._locator).click()

