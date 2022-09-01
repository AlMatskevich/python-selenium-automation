from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.driver.find_element(*self.ORDERS_BTN).click()