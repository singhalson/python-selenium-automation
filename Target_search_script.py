from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 3 A's
# Arrange
#init driver
driver = webdriver.Chrome()
driver.maximize_window()

#open the url
driver.get('https://www.target.com/')

# Act
driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

#verification / Assertion
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'

print('Test case passed')
driver.quit()


