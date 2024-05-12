import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import credentials


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def site(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    return driver


@pytest.fixture(scope='function')
def wait(site):
    return WebDriverWait(site, 5)


@pytest.fixture(scope="session")
def user_credentials():
    login = credentials.login()
    password = credentials.password()
    return login, password
