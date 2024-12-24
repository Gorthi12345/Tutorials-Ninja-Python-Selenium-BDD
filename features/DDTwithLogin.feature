Feature: Login Functionality with multiple sets of data
  Scenario Outline: Login with Correct Credientials
    Given I got navigated to login page
    When I will enter the valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on the login button
    Then I should get logged in
    Examples:
      | email                                            | password      |
      |redsea@gmail.com                                  |killingdevara  |
      |bvjanannlionabsbkjbbib@gmail.com                  |123455689      |
      |bvradevakathaaculionkjsbkjbbib@gmail.com          |123455689      |