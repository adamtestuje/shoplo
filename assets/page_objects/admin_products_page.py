# coding=utf-8
import time

from assets.page_objects.locators import AdminPageLocators
from base_page import BasePage


class AdminProductsPage(BasePage):
    def __init__(self, driver, store_name):
        BasePage.__init__(self, driver)
        self.url = "https://%s.shoplo.com/admin/products" % store_name


    def open_product_modal(self):
        buttons_add_product = self.driver.find_elements(*AdminPageLocators.BUTTONS_ADD_PRODUCT)
        buttons_add_product[0].click()
        return AdminProductsAddModal(self.driver)


class AdminProductsAddModal(BasePage):  # Another file would be better but it is big anyway.
    def add_product(self, product):
        self.fill_new_product_part(product["name"],
                                   product["description"],
                                   product["image"],
                                   product["visibility"],
                                   product["sku"])
        self.fill_price_part(product["price"],
                             product["price_type"],
                             product["tax_type"],
                             product["tax_amount"])
        self.toggle_advanced_view()                           # I'm not saying it is pretty. I'm saying it is readable.
        self.fill_stock(product["qty"],
                        product["buy_if_empty"])
        self.fill_additional_info(product["short_description"],
                                  product["weight"],
                                  product["width"],
                                  product["height"],
                                  product["depth"],
                                  product["diameter"],
                                  product["require_shipping"],
                                  product["vendor"],
                                  product["tag"])
        self.fill_seo(product["seo_address"],
                      product["seo_title"],
                      product["seo_keywords"],
                      product["seo_description"])
        self.click_button_submit()

    def fill_new_product_part(self, name, description, image, visibility, sku):
        self.fill_product_name(name)
        self.fill_product_description(description)
        self.attach_image(image)
        self.select_visibility(visibility)
        self.fill_product_sku(sku)

    def fill_price_part(self, price, price_type, tax_type, tax_amount):
        self.fill_price(price)
        self.select_price_type(price_type)
        self.select_tax_type(tax_type)
        self.fill_tax_amount(tax_amount)

    def fill_stock(self, qty, buy_if_empty):
        self.fill_qty(qty)
        self.check_buy_if_empty(buy_if_empty)

    def fill_additional_info(self, short_description, weight, width, height, depth,diameter, require_shipping, vendor,
                             tag):
        self.fill_short_description(short_description)
        self.fill_weight(weight)
        self.fill_width(width)
        self.fill_height(height)
        self.fill_depth(depth)
        self.fill_diameter(diameter)
        self.select_require_shipping(require_shipping)
        self.add_tag(tag)
        self.select_collection()
        self.select_vendor(vendor)

    def fill_seo(self, address, title, keywords, description):
        self.fill_seo_address(address)
        self.fill_seo_title(title)
        self.fill_seo_keywords(keywords)
        self.fill_seo_description(description)

    def fill_product_name(self, name):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_NAME, name)

    def fill_product_description(self, description):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_DESCRIPTION, description)

    def attach_image(self, image):
        self.attach_file(AdminPageLocators.INPUT_PRODUCT_IMAGE, image)

    def select_visibility(self, visibility):
        if not visibility:
            self.select_option(AdminPageLocators.SELECTOR_PRODUCT_VISIBILITY, "0")

    def fill_product_sku(self, sku):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_SKU, sku)

    def fill_price(self, price):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_PRICE, price)

    def select_price_type(self, price_type):
        self.select_option(AdminPageLocators.INPUT_PRODUCT_PRICE_TYPE, price_type)

    def select_tax_type(self, tax_type):
        self.select_option(AdminPageLocators.INPUT_PRODUCT_TAX_TYPE, tax_type)

    def fill_tax_amount(self, tax_amount):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_TAX_AMOUNT, tax_amount)

    def fill_qty(self, qty):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_STOCK_QTY, qty)

    def check_buy_if_empty(self, buy_if_empty):
        if buy_if_empty:
            self.check_element(AdminPageLocators.CHECKBOX_PRODUCT_BUY_IF_EMPTY)

    def fill_short_description(self, short_description):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_SHORT_DESCRIPTION, short_description)

    def fill_weight(self, weight):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_WEIGHT, weight)

    def fill_width(self, width):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_WIDTH, width)

    def fill_height(self, height):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_HEIGHT, height)

    def fill_depth(self, depth):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_DEPTH, depth)

    def fill_diameter(self, diameter):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_DIAMETER, diameter)

    def select_require_shipping(self, require_shipping):
        if not require_shipping:
            self.click_radio(AdminPageLocators.RADIO_PRODUCT_NOT_REQUIRE_SHIPPING)
        else:
            self.click_radio(AdminPageLocators.RADIO_PRODUCT_REQUIRE_SHIPPING)

    def add_tag(self, tag):
        self.fill_input(AdminPageLocators.INPUT_PRODUCT_TAG, tag)
        self.click_button(AdminPageLocators.BUTTON_PRODUCT_ADD_TAG)

    def select_collection(self):
        self.select_first_collection()
        """
        So, I will just select the first collection. I have found out that this part of the system not behave
        regularly. I have no idea if you implemented it this way by some reason, but if not I guess you should take a
        look.
        """

    def select_vendor(self, vendor):
        if vendor:
            self.select_option(AdminPageLocators.SELECTOR_PRODUCT_VENDOR, vendor)
        """
        Here I will just implement logic.
        Why? Adding vendor to merchant was out of scope of the task.
        """

    def fill_seo_address(self, address):
        self.fill_input(AdminPageLocators.INPUT_SEO_ADDRESS, address)

    def fill_seo_title(self, title):
        self.fill_input(AdminPageLocators.INPUT_SEO_TITLE, title)

    def fill_seo_keywords(self, keywords):
        self.fill_input(AdminPageLocators.INPUT_SEO_KEYWORDS, keywords)

    def fill_seo_description(self, description):
        self.fill_input(AdminPageLocators.INPUT_SEO_DESCRIPTION, description)

    def click_button_submit(self):
        self.click_button(AdminPageLocators.BUTTON_SUBMIT)

    def select_first_collection(self):
        """ - if available. Randomness here is a miracle. ( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ """
        all_collections = self.driver.find_elements(*AdminPageLocators.CHECKBOXES_PRODUCT_COLLECTION_1)
        if all_collections:
            all_collections[0].click()

    def toggle_advanced_view(self):
        self.click_link(AdminPageLocators.LINK_PRODUCT_ADVANCED_VIEW)
