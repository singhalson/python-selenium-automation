Feature: Tests for Cart functionality

Scenario: Verify Target Cart is empty
    Given Open Target main page
    When Target home page is opened
    When Open Cart page
    Then Verify "Your cart is empty" message is shown


  Scenario: Verify that cart has individual items
    Given Open Target main page
    Then Search for a tea
    When Select the product
    And Add the product to the cart & view cart
    Then Search for Tea
    And Select the product
    When Click Add to cart button
    And Open Cart page
    Then Verify cart has individual items