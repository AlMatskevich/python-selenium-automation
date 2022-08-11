Feature: Tests for amazon privacy notice

Scenario: User can open and close amazon privacy notice
  Given Open Amazon T&C page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  And Switch back to original

