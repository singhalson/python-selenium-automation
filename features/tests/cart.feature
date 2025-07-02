# Created by Owner at 6/29/2025
Feature: Cart tests
  # Enter feature description here

#Scenario: User can click on the cart icon
#    Given Open target main page
#    When Clicked on cart icon
#    Then Verify 'Your cart is empty' message is shown

Scenario: Verify that cart has individual items
    Given Open target main page
    When Search for tea
   # Then Select the product
    Then Add the product to the cart and view cart
