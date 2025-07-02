from selenium.webdriver.common.by import By
from behave import given, when, then

from Target_Homework2 import actual


@then("Verify 'Your cart is empty' message is shown")
def verify_message_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error, expected '{expected_text}' but got '{actual_text}'"

@then('Add the product to the cart and view cart')
def add_to_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='chooseOptionsButton']").click()

