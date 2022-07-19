
Feature: Sign in test cases


  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click Cart
    Then Verify Amazon Cart is empty