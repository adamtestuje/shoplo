from selenium.webdriver.common.by import By


class Common():
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')


class AdminSidebarMenuLocators():
    # Admin sub-page
    LINK_PRODUCTS = (By.ID, 'productListSidebar')


class AdminPageLocators():
    # Products sub-page
    BUTTONS_ADD_PRODUCT = (By.LINK_TEXT, "Product")
    # Products sub-page / Add modal
    INPUT_PRODUCT_NAME = (By.ID, "name")
    INPUT_PRODUCT_DESCRIPTION = (By.ID, "redactor-uuid-0")
    INPUT_PRODUCT_IMAGE = (By.XPATH, "//input[@type='file']")
    SELECTOR_PRODUCT_VISIBILITY = (By.ID, "visibility")
    INPUT_PRODUCT_SKU = (By.ID, "sku")
    INPUT_PRODUCT_PRICE = (By.ID, "price")
    INPUT_PRODUCT_PRICE_TYPE = (By.ID, "price-type")
    INPUT_PRODUCT_TAX_TYPE = (By.ID, "tax_type")
    INPUT_PRODUCT_TAX_AMOUNT = (By.ID, "tax")
    LINK_PRODUCT_ADVANCED_VIEW = (By.LINK_TEXT, "Basic View / Advanced view")
    CHECKBOX_PRODUCT_STOCK_TRACKING = (By.ID, "add_to_stock")
    INPUT_PRODUCT_STOCK_QTY = (By.ID, "quantity")
    CHECKBOX_PRODUCT_BUY_IF_EMPTY = (By.XPATH, "//input[@id='buy_if_empty']/following-sibling::label")
    INPUT_PRODUCT_SHORT_DESCRIPTION = (By.ID, "short_description")
    INPUT_PRODUCT_WEIGHT = (By.ID, "weight")
    INPUT_PRODUCT_WIDTH = (By.ID, "width")
    INPUT_PRODUCT_HEIGHT = (By.ID, "height")
    INPUT_PRODUCT_DEPTH = (By.ID, "depth")
    INPUT_PRODUCT_DIAMETER = (By.ID, "diameter")
    RADIO_PRODUCT_REQUIRE_SHIPPING = (By.XPATH, "//input[@id='require_shipping']/parent::li")
    RADIO_PRODUCT_NOT_REQUIRE_SHIPPING = (By.XPATH, "//input[@id='not_require_shipping']/parent::li")
    INPUT_PRODUCT_TAG = (By.ID, "tag")
    BUTTON_PRODUCT_ADD_TAG = (By.XPATH, "//input[@id='tag']/following-sibling::button")
    CHECKBOXES_PRODUCT_COLLECTION_1 = (By.XPATH, "//input[@name='collections[]']/parent::li/parent::ul")
    SELECTOR_PRODUCT_VENDOR = (By.ID, "vendor")
    INPUT_SEO_ADDRESS = (By.ID, "page-url")
    INPUT_SEO_TITLE = (By.ID, "page-title")
    INPUT_SEO_KEYWORDS = (By.ID, "page-keywords")
    INPUT_SEO_DESCRIPTION = (By.ID, "page-description")
    BUTTON_SUBMIT = (By.XPATH, '//section[@id="add-product-layer"]//button[@type="submit"]')


class RegisterPageLocators(Common):
    # First step
    INPUT_STORE_NAME = (By.ID, 'storeName')
    INPUT_STORE_EMAIL = (By.ID, 'storeEmail')
    INPUT_STORE_PASSWORD = (By.ID, 'storePassword')
    # Second step
    INPUT_USER_NAME = (By.NAME, 'name')
    INPUT_USER_PHONE = (By.NAME, 'phone')
    SELECTOR_COUNTRY = (By.NAME, 'country')
    SELECTOR_SELL_ONLINE = (By.ID, 'sell_online')
    SELECTOR_WHY = (By.ID, 'why_testing')
    SELECTOR_HOW = (By.ID, 'hear_about')


class LoginPageLocatiors(Common):
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
