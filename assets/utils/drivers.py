from selenium import webdriver


class Drivers:
    @staticmethod
    def get_driver(browser):
        return {
            'chrome':  webdriver.Chrome()
        }[browser]
        # Usually I make some getters for each driver / config.
