from utilities.base_class import BaseClass
from pageobjects.homepage import HomePage
import time


class TestStartPractising(BaseClass):

    def test_start_practicing(self, driver):
        homepage = HomePage(driver)
        homepage.start_practicing()
        time.sleep(10)


