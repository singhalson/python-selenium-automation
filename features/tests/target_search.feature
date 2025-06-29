# Created by Owner at 6/28/2025
Feature: Test for target Search
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked

  Scenario: User can click on the cart icon
    Given Open target main page
    When Clicked on cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: User can signin after logging out
    Given Open target main page
    When Click signin
    When Click signin from the right side
    Then Verify 'sign into your Target account' page opens