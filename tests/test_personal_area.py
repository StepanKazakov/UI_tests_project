from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators
from test_login_page import test_login_from_login_button as LOGIN


def test_enter_to_personal_area(site):
    LOGIN(site)  # Do login
    # Enter to personal area
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until page download and check credentials in inputs
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_save_btn)))
    assert site.find_element(By.XPATH, locators.profile_name).get_attribute('value') == 'Test User'


def test_pass_to_constructor_from_personal_area(site):
    LOGIN(site)  # Do login
    # Enter to personal area
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until page download and click constructor to pass, check transition to constructor page
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_save_btn)))
    site.find_element(By.XPATH, locators.header_constructor_btn).click()
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'


def test_pass_to_constructor_by_logo(site):
    LOGIN(site)  # Do login
    # Enter to personal area
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until page download and click constructor to pass, check transition to constructor page
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_save_btn)))
    site.find_element(By.XPATH, locators.header_logo_btn).click()
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
           site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'


def test_logout_from_personal_area(site):
    LOGIN(site)  # Do login
    # Enter to personal area
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
    site.find_element(By.XPATH, locators.header_personal_area_btn).click()
    # Wait until page download and click logout, check transition to login page
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_save_btn)))
    site.find_element(By.XPATH, locators.profile_logout_btn).click()
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
    assert site.current_url == 'https://stellarburgers.nomoreparties.site/login'
