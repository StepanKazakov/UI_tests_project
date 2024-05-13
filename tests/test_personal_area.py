from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestPersonalAreaScenarios:
    @staticmethod
    def login(site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
        site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
        site.find_element(By.XPATH, locators.input_email).send_keys('kazakovstepan1262@ya.ru')
        site.find_element(By.XPATH, locators.input_password).send_keys('123456')
        site.find_element(By.XPATH, locators.login_btn).click()

    def test_enter_to_personal_area(self, site):
        self.login(site)
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_logout_btn)))
        assert site.find_element(By.XPATH, locators.input_name).get_attribute('value') == 'Test User'

    def test_pass_to_constructor_from_personal_area(self, site):
        self.login(site)
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_logout_btn)))
        site.find_element(By.XPATH, locators.header_constructor_btn).click()
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
               site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'

    def test_pass_to_constructor_by_logo(self, site):
        self.login(site)
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_logout_btn)))
        site.find_element(By.XPATH, locators.header_logo_btn).click()
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
               site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'

    def test_logout_from_personal_area(self, site):
        self.login(site)
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.profile_logout_btn)))
        site.find_element(By.XPATH, locators.profile_logout_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/login'
