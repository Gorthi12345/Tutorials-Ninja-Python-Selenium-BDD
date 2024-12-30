Feature: Login Functionality
  @only
  Scenario: Login with Correct Credientials
    Given I got navigated to login page
    When I will enter the valid email address as "redsea@gmail.com" and valid password as "killingdevara" into the fields
    And I click on the login button
    Then I should get logged in
  @cheater
  Scenario: Login with Invalid email address and valid Password
    Given I got navigated to login page
    When I will enter the Invalid email address and valid password into the fields
    And I click on the login button
    Then I should get a proper error message
  Scenario: Login with valid email address and Invalid Password
    Given I got navigated to login page
    When I will enter the valid email address and Invalid password into the fields
    And I click on the login button
    Then I should get a proper error message
  Scenario: Login with Incorrect Credientials
    Given I got navigated to login page
    When I will enter the Invalid email address and Invalid password into the fields
    And I click on the login button
    Then I should get a proper error message
  Scenario: Login with WithOut Credientials
    Given I got navigated to login page
    When I do not enter the email address and password into the fields
    And I click on the login button
    Then I should get a proper error message