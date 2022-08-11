from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


PRIVACY_NOTICE_LINK = (By.XPATH, "//a[contains(text(), 'Privacy Notice')]")


@given('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_on_tc_link(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(PRIVACY_NOTICE_LINK), message='Privacy notice link is not clickable'
    ).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current window', context.driver.current_window_handles)
    new_window = context.driver.current_window_handles[1]
    context.driver.switch_to_.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    sleep(2)
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window')
def close_notice_page(context):
    context.driver.close()


@then('Switch back to original')
def switch_back(context):
    context.driver.switch_to.window(context.original_window)