from assets.page_objects.admin_products_page import AdminProductsPage
from assets.page_objects.locators import AdminSidebarMenuLocators
from base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, driver, store_name):
        BasePage.__init__(self, driver)
        self.store_name = store_name

    def open_products_page(self):
        self.click_link(AdminSidebarMenuLocators.LINK_PRODUCTS)
        return AdminProductsPage(self.driver, self.store_name)
