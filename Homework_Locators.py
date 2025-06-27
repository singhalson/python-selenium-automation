from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#by Xpath, Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#by ID, email field
driver.find_element(By.ID, 'ap_email_login')

#By XPath, Continue button
driver.find_element(By.XPATH, '//input[@aria-labelledby="continue-announce"]')

#By text, conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#By text, Privacy Notice link
driver.find_element(By.XPATH, "//a[text()= 'Privacy Notice']")

#By partial match, Need help link
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=unified_claim_collections')]")

#By ID, create your Amazon account
driver.find_element(By.ID, 'createAccountSubmit')

#no link for 'forgot your password' and 'other issues with sign-in'

