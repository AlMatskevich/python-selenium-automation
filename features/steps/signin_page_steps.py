from selenium.webdriver.common.by import By
from behave import given, when, then

@then ('Verify Sign in page opened')
def verify_sign_in_page_opened(context):
    expected_text = 'Sign-In'
    actual_text = context.driver.find_element(By.XPATH, "//h1 [@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    # Verify email field is present
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed()

@then ('Verify Amazon Cart is empty')
def verify_cart_is_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').is_displayed()

