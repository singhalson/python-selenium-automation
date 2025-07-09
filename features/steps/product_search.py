from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.ID, 'search')
def open_target(context):

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search = context.driver.wait.until(EC.presence_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)
    sleep(2)

@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()


@then('Product results for {search_word} are shown')