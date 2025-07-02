from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click signin')
def click_on_signin(context):
    context.driver.find_element(By.CSS_SELECTOR,"styles_ndsCol__MIQSp.styles_xs__jQ_Rd.styles_md__OYQNi.styles_lg__ztoXN.styles_xl__uig4J").click()

@when('Click signin from the right side')
def click_signin_in_the_form(context):
    context.driver.find_element(By.ID, 'login').click()

@then('Select the product')
def select_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").click()


@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"

@then("Verify 'sign into your Target account' page opens")
def verify_user(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "styles_ndsHeading_HcGpD.styles_fontSize2__8Iex_.styles_x2Margin__M5gHh.sc-93cdbffc-2.denKZZ").text()
    expected_text = 'Sign into your Target account'
    assert actual_text == expected_text, f"Error, expected '{expected_text}' but got '{actual_text}'"