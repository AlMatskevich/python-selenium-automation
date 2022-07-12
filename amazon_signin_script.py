from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="D:\Automation\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,"//span [@class='nav-line-2' and text()='& Orders']").click()

expected_result1 = 'Sign-In'
actual_result1 = driver.find_element(By.XPATH, "//h1 [@class='a-spacing-small']").text
assert expected_result1 == actual_result1, f'Expected {expected_result1} but got {actual_result1}'

print('Test case "Sign In header is visible" pass')


expected_result2 = 'email'
actual_result2 = driver.find_element(By.XPATH, "//input [@type='email']").text
assert expected_result2 == actual_result2, f'Expected {expected_result2} but got {actual_result2}'


driver.quit()
