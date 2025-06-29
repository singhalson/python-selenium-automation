from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"


@when('Clicked on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLink']").click()

@then("Verify 'Your cart is empty' message is shown")
def verify_message_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error, expected '{expected_text}' but got '{actual_text}'"

@when('Click signin')
def click_on_signin(context):
    context.driver.find_element(By.CSS_SELECTOR,"styles_ndsCol__MIQSp.styles_xs__jQ_Rd.styles_md__OYQNi.styles_lg__ztoXN.styles_xl__uig4J").click()

@when('Click signin from the right side')
def click_signin_in_the_form(context):
    context.driver.find_element(By.ID, 'login').click()

@then("Verify 'sign into your Target account' page opens")
def verify_user(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "styles_ndsHeading_HcGpD.styles_fontSize2__8Iex_.styles_x2Margin__M5gHh.sc-93cdbffc-2.denKZZ").text()
    expected_text = 'Sign into your Target account'
    assert actual_text == expected_text, f"Error, expected '{expected_text}' but got '{actual_text}'"