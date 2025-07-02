from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'search').send_keys(search_word)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(30)


@when('Clicked on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLink']").click()