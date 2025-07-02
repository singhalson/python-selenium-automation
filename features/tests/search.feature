# Created by Owner at 6/28/2025
Feature: Test for target Search
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario: User can search for a mug on Target
    Given Open target main page
    When Search for mug
    Then Verify search worked for mug

  Scenario: User can search for a coffee on Target
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee




  Scenario: User can signin after logging out
    Given Open target main page
    When Click signin
    When Click signin from the right side
    Then Verify 'sign into your Target account' page opens