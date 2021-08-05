from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.seleniumeasy.com/test/")
    driver.maximize_window()
    yield driver
    driver.close()
