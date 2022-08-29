from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given ('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@when ('Click on Add to cart button')
def click_add_to_cart(context,):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)


@then ('Verify user can click through all colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Khaki Brown', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash', 'Washed Black', 'Washed Grey']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    actual_colors = []
    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print('Actual colors:', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'

