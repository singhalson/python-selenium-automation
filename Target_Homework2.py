from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#open target
driver.get('https://www.target.com/')

#search the field
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

#verification
expected = 'Sign in or create account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading'])").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'


driver.find_element(By.ID, 'login')




