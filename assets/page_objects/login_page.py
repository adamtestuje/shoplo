from admin_page import AdminPage
from base_page import BasePage
from locators import LoginPageLocatiors


class LoginPage(BasePage):
    def __init__(self, driver, store_name):
        BasePage.__init__(self, driver)
        self.store_name = store_name
        self.url = "https://%s.shoplo.com/admin" % store_name

    def login_as(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit()
        return AdminPage(self.driver, self.store_name)

    def fill_email(self, email):
        self.fill_input(LoginPageLocatiors.INPUT_EMAIL, email)

    def fill_password(self, password):
        self.fill_input(LoginPageLocatiors.INPUT_PASSWORD, password)

    def submit(self):
        self.click_button(LoginPageLocatiors.BUTTON_SUBMIT)
