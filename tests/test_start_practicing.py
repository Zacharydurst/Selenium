import pytest
from utilities.base_class import BaseClass
from pageobjects.homepage import HomePage


class TestStartPractising(BaseClass):

    def test_start_practicing(self, driver):
        homepage = HomePage(driver)
        homepage.click_button(homepage.start_practicing)

