from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from controls.button import Button


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self._title = (By.CSS_SELECTOR, 'div#site-name a')
        self._start_practicing_button = Button(self.driver, by=By.CSS_SELECTOR, selector='#btn_basic_example')

    def read_title(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self._title))
        return self.driver.find_element(*self._title).text

    def start_practicing(self):
        self._start_practicing_button.click()
