import os
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def fill_input(self, locator, value):
        self.find_element(locator).send_keys('')
        self.find_element(locator).send_keys(str(value))

    def read_input(self, locator):
        return self.driver.find_element(*locator).get_attribute('value')

    def check_element(self, locator):
        self.driver.find_element(*locator).click()

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def click_link(self, locator):
        self.driver.find_element(*locator).click()

    def click_radio(self, locator):
        self.driver.find_element(*locator).click()

    def select_option(self, selector, option):
        selector_element = self.driver.find_element(*selector)
        Select(selector_element).select_by_value(str(option))

    def attach_file(self, locator, file_path):
        print "I will attach following file now: " + (os.getcwd()+file_path)
        self.driver.find_element(*locator).send_keys(os.getcwd()+file_path)

    def find_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(visibility_of_element_located(locator))
        return element

    def navigate(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def actual_title(self):
        return self.driver.title

    def actual_text(self):
        return self.driver.page_source

    def actual_url(self):
        return self.url
