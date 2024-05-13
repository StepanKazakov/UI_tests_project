from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestConstructorCategories:
    @staticmethod
    def wait_and_click_category(site, category_button_locator):
        # Wait until the category button is clickable and then click it
        WebDriverWait(site, 5).until(EC.element_to_be_clickable((By.XPATH, category_button_locator)))
        site.find_element(By.XPATH, category_button_locator).click()

    @staticmethod
    def assert_tab_has_selected_class(site, category_button_locator):
        # Wait for the parent div of the category button to be visible and check if it has the 'selected' class
        parent_div_locator = category_button_locator + '/..'
        WebDriverWait(site, 5).until(EC.visibility_of_element_located((By.XPATH, parent_div_locator)))
        assert site.find_element(By.XPATH, parent_div_locator).get_attribute('class') == \
               'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_constructor_choose_bread_category(self, site):
        # Select first sauce then bread category (because bread is default)
        self.wait_and_click_category(site, locators.cons_sauce_btn)
        self.wait_and_click_category(site, locators.cons_bread_btn)
        self.assert_tab_has_selected_class(site, locators.cons_bread_btn)

    def test_constructor_choose_sauce_category(self, site):
        # Select sauce category
        self.wait_and_click_category(site, locators.cons_sauce_btn)
        self.assert_tab_has_selected_class(site, locators.cons_sauce_btn)

    def test_constructor_choose_filling_category(self, site):
        # Select filling category
        self.wait_and_click_category(site, locators.cons_filling_btn)
        self.assert_tab_has_selected_class(site, locators.cons_filling_btn)
