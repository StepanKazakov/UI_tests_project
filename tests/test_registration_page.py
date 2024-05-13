from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import credentials
import locators


class TestRegistrationScenarios:
    def test_registration_with_random_data(self, site):
        # Navigate to registration
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
        site.find_element(By.XPATH, locators.do_register).click()
        # Fill the registration form with randomly generated valid data
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.register_btn)))
        site.find_element(By.XPATH, locators.input_name).send_keys('VIP client')
        site.find_element(By.XPATH, locators.input_email).send_keys(credentials.login())
        site.find_element(By.XPATH, locators.input_password).send_keys(credentials.password())
        site.find_element(By.XPATH, locators.register_btn).click()
        # Verify redirection to login page
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.login_btn)))
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_with_incorrect_password_get_mistake(self, site):
        # Navigate to registration
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.header_personal_area_btn)))
        site.find_element(By.XPATH, locators.header_personal_area_btn).click()
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.do_register)))
        site.find_element(By.XPATH, locators.do_register).click()
        # Fill the registration form with incorrect password (less than 6 symbols)
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, locators.register_btn)))
        site.find_element(By.XPATH, locators.input_name).send_keys('wrong client')
        site.find_element(By.XPATH, locators.input_email).send_keys('123@ya.ru')
        site.find_element(By.XPATH, locators.input_password).send_keys(credentials.wrong_password())
        site.find_element(By.XPATH, locators.register_btn).click()
        # Ensure that the user stays on the registration page and receives an error message
        assert site.current_url == 'https://stellarburgers.nomoreparties.site/register' and \
               site.find_element(By.XPATH, locators.incorrect_password).text == 'Некорректный пароль'
