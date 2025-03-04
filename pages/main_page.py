from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Search for {search_word} on amazon')
def search_product(context, search_word):
    context.app.header.search_product(search_word)


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()
@when('Click on button from SignIn popup')


def click_sign_in_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='SignIn not clickable'
    ).click()


@when('Wait for {sec} sec') # '8'
def sleep_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In is clickable')
def verify_sign_in_btn_clickable(context):
    context.driver.wait.until(
        EC.presence_of_element_located(SIGN_IN_POPUP_BTN), message='SignIn not clickable'
    )

