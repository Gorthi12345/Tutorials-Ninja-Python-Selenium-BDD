Feature: Login Functionality with Excel Data

  Scenario Outline: : Login with Credientials
    Given I got navigated to login
    When I am entering the email address as "<email>" and valid password as "<password>" into the fields
    And I click on the login
    Then Get into the website if the credientials or correct
    Examples:
      | email | password |
