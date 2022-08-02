from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BESTSELLERS = (By.CSS_SELECTOR, '#zg_header a')


@given('Open Amazon BestSellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then ('Verify there are {expected_amount} links')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLERS)

    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
