from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

@when ('Click on the first product')
def open_amazon(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

'''''@then ('User sees results for {expected result}')
def verify_search_results(context,expected result):
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f'Expected {expected_result1} but got {actual_result1}'''