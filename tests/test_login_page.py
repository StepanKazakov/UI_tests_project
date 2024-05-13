from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestLoginScenarios:
    login = 'kazakovstepan1262@ya.ru'
    password = '123456'

    @staticmethod
    def fill_login_details_and_submit(site, login, password):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
        site.find_element(By.XPATH, locators.input_email).send_keys(login)
        site.find_element(By.XPATH, locators.input_password).send_keys(password)
        site.find_element(By.XPATH, locators.login_btn).click()

    def assert_login_successful(self, site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/' and \
               site.find_element(By.XPATH, locators.login_or_make_order_btn).text == 'Оформить заказ'

    def test_login_from_login_button(self, site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
        site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
        self.fill_login_details_and_submit(site, self.login, self.password)
        self.assert_login_successful(site)

    def test_login_to_personal_area(self, site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        self.fill_login_details_and_submit(site, self.login, self.password)
        self.assert_login_successful(site)

    def test_login_from_registration_page(self, site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
        site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
        site.find_element(By.XPATH, locators.do_register).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_link)))
        site.find_element(By.XPATH, locators.login_link).click()
        self.fill_login_details_and_submit(site, self.login, self.password)
        self.assert_login_successful(site)

    def test_login_from_password_recovery_page(self, site):
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_or_make_order_btn)))
        site.find_element(By.XPATH, locators.login_or_make_order_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.password_recovery)))
        site.find_element(By.XPATH, locators.password_recovery).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_link)))
        site.find_element(By.XPATH, locators.login_link).click()
        self.fill_login_details_and_submit(site, self.login, self.password)
        self.assert_login_successful(site)
