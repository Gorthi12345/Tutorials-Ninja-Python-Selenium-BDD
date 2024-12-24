Feature: Search Functionality
  @cheating
  Scenario: Search the Valid Product
    Given I got navigated to Home Screen
    When I entered the valid input to the Search Box
    And Click on the Search Button
    Then Valid Product Should get displayed in the results
  Scenario: Search the InValid Product
    Given I got navigated to Home Screen
    When I entered the InValid input to the Search Box
    And Click on the Search Button
    Then Proper message should be get displayed in the results
  Scenario: Search Without the input
    Given I got navigated to Home Screen
    When I do not enter the input in the search box
    And Click on the Search Button
    Then Proper message should be get displayed in the results