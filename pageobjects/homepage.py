from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from controls.button import Button


class HomePage:

    title = (By.CSS_SELECTOR, 'div#site-name a')
    start_practicing = (By.CSS_SELECTOR, '#btn_basic_example')

    def __init__(self, driver):
        self.driver = driver

    def read_title(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(HomePage.title))
        return self.driver.find_element(*HomePage.title).text

    def click_button(self):
        button = Button(self.driver)
        button.click_button()
