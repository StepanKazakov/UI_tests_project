import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


@pytest.mark.order(11)
def test_constructor_choose_bread_category(site):
    # Wait until the category buttons is clickable and then click on sauce (for scroll), click on bread for return
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.constructor_bread_btn)))
    site.find_element(By.XPATH, locators.constructor_sauce_btn).click()
    site.find_element(By.XPATH, locators.constructor_bread_btn).click()
    time.sleep(2)  # Wait for scrolling finish
    # Check if bread title is directly below category buttons
    location_buttons = site.find_element(By.XPATH, locators.constructor_category_buttons).location
    location_title = site.find_element(By.XPATH, locators.constructor_bread_title).location
    category_buttons_height = site.find_element(By.XPATH, locators.constructor_category_buttons).size['height']
    assert (location_title['y'] > location_buttons['y']) and \
           ((location_title['y'] - location_buttons['y']) <= (category_buttons_height + 2))


@pytest.mark.order(12)
def test_constructor_choose_sauce_category(site):
    # Wait until the category buttons is clickable and then click on sauce
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.constructor_sauce_btn)))
    site.find_element(By.XPATH, locators.constructor_sauce_btn).click()
    time.sleep(2)  # Wait for scrolling finish
    # Check if sauce title is directly below category buttons
    location_buttons = site.find_element(By.XPATH, locators.constructor_category_buttons).location
    location_title = site.find_element(By.XPATH, locators.constructor_sauce_title).location
    category_buttons_height = site.find_element(By.XPATH, locators.constructor_category_buttons).size['height']
    assert (location_title['y'] > location_buttons['y']) and \
           ((location_title['y'] - location_buttons['y']) <= (category_buttons_height + 2))


@pytest.mark.order(13)
def test_constructor_choose_filling_category(site):
    # Wait until the category buttons is clickable and then click on filling
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.constructor_filling_btn)))
    site.find_element(By.XPATH, locators.constructor_filling_btn).click()
    time.sleep(2)  # Wait for scrolling finish
    # Check if filling title is directly below category buttons
    location_buttons = site.find_element(By.XPATH, locators.constructor_category_buttons).location
    location_title = site.find_element(By.XPATH, locators.constructor_filling_title).location
    category_buttons_height = site.find_element(By.XPATH, locators.constructor_category_buttons).size['height']
    assert (location_title['y'] > location_buttons['y']) and \
           ((location_title['y'] - location_buttons['y']) <= (category_buttons_height + 2))
