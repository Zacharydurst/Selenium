import pytest
from utilities.base_class import BaseClass
from pageobjects.homepage import HomePage


class TestLocateTitle(BaseClass):

    def test_locate_title(self, driver):
        homepage = HomePage(driver)
        assert homepage.read_title() == 'Selenium Easy'
