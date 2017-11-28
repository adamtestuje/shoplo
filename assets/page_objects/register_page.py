from base_page import BasePage
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    url = 'https://store.shoplo.com/register'

    def register_new_user(self, merchant):
        self.driver.get("https://store.shoplo.com/register")
        self.fill_first_step(merchant["store_name"], merchant["store_email"], merchant["store_password"])
        self.submit()
        self.fill_second_step(merchant["user_name"], merchant["user_phone"], merchant["user_country"])
        self.submit()

    def fill_first_step(self, store_name, store_email, store_password):
        self.fill_input(RegisterPageLocators.INPUT_STORE_NAME, store_name)
        self.fill_input(RegisterPageLocators.INPUT_STORE_EMAIL, store_email)
        self.fill_input(RegisterPageLocators.INPUT_STORE_PASSWORD, store_password)

    def fill_second_step(self, user_name, user_phone, user_country):
        self.fill_input(RegisterPageLocators.INPUT_USER_NAME, user_name)
        self.fill_input(RegisterPageLocators.INPUT_USER_PHONE, user_phone)
        self.set_country(user_country)
        self.set_own_products('just_starting')  # It's just faster to hard-code it for now.
        self.set_why('playing_around')          # I hope you get me earlier.
        self.set_how('other')                   #

    def set_country(self, country):
        self.select_option(RegisterPageLocators.SELECTOR_COUNTRY, country)

    def set_own_products(self, option):
        self.select_option(RegisterPageLocators.SELECTOR_SELL_ONLINE, option)

    def set_why(self, option):
        self.select_option(RegisterPageLocators.SELECTOR_WHY, option)

    def set_how(self, option):
        self.select_option(RegisterPageLocators.SELECTOR_HOW, option)

    def submit(self):
        self.click_button(RegisterPageLocators.BUTTON_SUBMIT)
