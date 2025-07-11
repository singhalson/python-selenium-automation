# Created by Owner at 7/10/2025
Feature: Tests for Sign In functionality

  Scenario: Navigate to Sign In page
    Given Open Target main page
    Then Click "Account" button
    And Click "Sign In" button
    And Verify Sign In form opened
