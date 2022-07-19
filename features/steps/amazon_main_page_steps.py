from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when ('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID,'nav-orders').click()

@when ('Click Cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()



