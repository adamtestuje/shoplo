# coding=utf-8
import unittest
from assets.page_objects.login_page import LoginPage
from assets.page_objects.register_page import RegisterPage
from assets.utils.data_store import DataStore
from assets.utils.drivers import Drivers


class TestSuite(unittest.TestCase):
    driver = None
    login_page = None
    merchant = DataStore().generate_merchant()
    product = DataStore().generate_product()

    @classmethod
    def setUpClass(cls):
        register_page = RegisterPage(cls.driver)
        register_page.register_new_user(cls.merchant)
        register_page.close()

    def setUp(self):
        self.driver = Drivers.get_driver('chrome')
        self.login_page = LoginPage(self.driver, self.merchant["store_normalized"])
        self.login_page.navigate()

    def tearDown(self):
        self.driver.quit()

    """
    Following part will test login page.
    """
    def test_can_login_given_valid_credentials(self):
        admin_page = self.login_page.login_as(self.merchant["store_email"], self.merchant["store_password"])
        self.assertEqual(self.merchant["store_name"].title(), admin_page.actual_title())

    def test_can_not_login_given_wrong_email(self):
        self.login_page.login_as("wrong@email.addr", self.merchant["store_password"])
        self.assertTrue("Invalid email addres and/or password" in self.login_page.actual_text())
        # There you got some small bug on   ^    production.

    def test_can_not_login_given_invalid_email(self):
        self.login_page.login_as("invalidMail", self.merchant["store_password"])
        self.assertTrue("Please enter a valid email address." in self.login_page.actual_text())
        # FYI: Your system is accepting e.g. "wrong@email" as a valid email address.

    def test_can_not_login_given_wrong_password(self):
        self.login_page.login_as(self.merchant["store_email"], "WrongPassw0rd")
        self.assertTrue("Invalid email addres and/or password" in self.login_page.actual_text())

    def test_can_not_login_given_no_data(self):
        self.login_page.login_as("", "")
        self.assertTrue("This field is required." in self.login_page.actual_text())

    """
    Following part will test the product cases.
    """
    def test_it_can_go_to_products_page(self):
        admin_page = self.login_page.login_as(self.merchant["store_email"], self.merchant["store_password"])
        products_page = admin_page.open_products_page()
        self.assertEqual(products_page.url, products_page.actual_url())

    def test_it_can_add_new_product(self):
        admin_page = self.login_page.login_as(self.merchant["store_email"], self.merchant["store_password"])
        products_page = admin_page.open_products_page()
        add_product_modal = products_page.open_product_modal()
        add_product_modal.add_product(self.product)
        self.assertTrue(self.product["name"] in products_page.actual_text())


if __name__ == "__main__":
    unittest.main()
