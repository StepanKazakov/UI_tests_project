from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


def test_constructor_choose_bread_category(site):
    # Wait until the category buttons is clickable and then click on sauce (for scroll), click on bread for return
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.cons_bread_btn)))
    site.find_element(By.XPATH, locators.cons_sauce_btn).click()
    site.find_element(By.XPATH, locators.cons_bread_btn).click()
    # Wait element and check if bread tab has selected class
    parent_div_locator = locators.cons_bread_btn + '/..'
    WebDriverWait(site, 5).until(EC.visibility_of_element_located((By.XPATH, parent_div_locator)))
    assert site.find_element(By.XPATH, parent_div_locator).get_attribute('class') == \
           'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


def test_constructor_choose_sauce_category(site):
    # Wait until the category buttons is clickable and then click on sauce
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.cons_sauce_btn)))
    site.find_element(By.XPATH, locators.cons_sauce_btn).click()
    # Wait element and check if sauce tab has selected class
    parent_div_locator = locators.cons_sauce_btn + '/..'
    WebDriverWait(site, 5).until(EC.visibility_of_element_located((By.XPATH, parent_div_locator)))
    assert site.find_element(By.XPATH, parent_div_locator).get_attribute('class') == \
           'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


def test_constructor_choose_filling_category(site):
    # Wait until the category buttons is clickable and then click on filling
    WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.cons_filling_btn)))
    site.find_element(By.XPATH, locators.cons_filling_btn).click()
    # Wait element and check if filling tab has selected class
    parent_div_locator = locators.cons_filling_btn + '/..'
    WebDriverWait(site, 5).until(EC.visibility_of_element_located((By.XPATH, parent_div_locator)))
    assert site.find_element(By.XPATH, parent_div_locator).get_attribute('class') == \
           'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
