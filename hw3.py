from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='chromedriver.exe')

#Locators for Create Account (Registration) page elements:
#Logo:
driver.find.element(By.CSS_SELECTOR, 'i.a-icon-logo')
#"Create account"
driver.find.element(By.CSS_SELECTOR, 'h1.a-spacing-small')
#"Your name" field
driver.find.element(By.CSS_SELECTOR, '#ap_customer_name')
#"Mobile number or email" field
driver.find.element(By.CSS_SELECTOR, '#ap_email')
#"Password" field
driver.find.element(By.CSS_SELECTOR, '#ap_password')
#"Re-enter password" field
driver.find.element(By.CSS_SELECTOR, '#ap_password')
#"Mobile number or email" field
driver.find.element(By.CSS_SELECTOR, '#ap_password_check')
#"Continue" button
driver.find.element(By.CSS_SELECTOR, '#continue')
#"Conditions of Use"
driver.find.element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
#"Privacy Notice"
driver.find.element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")
#"Sign-In"
driver.find.element(By.CSS_SELECTOR, "a[href*='open']")

