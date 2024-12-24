Feature: Register Account Functionality
  @registered
  Scenario: Register with Mandatory Fields
    Given I navigated to the register page
    When I entered the details into the all mandatory fields
      |first_name|last_name|email                |telephone|password|confirm_password|
      |simba     |mufasa   |m|100000000|Scar    |Scar            |
    And Click on the continue
    Then Account Should get Created

  Scenario: Register with all Fields
    Given I navigated to the register page
    When I entered the details into the all fields
    And Click on the continue
    Then Account Should get Created
  Scenario: Register with Duplicate email address
    Given I navigated to the register page
    When I entered the details except email address
    And I entered the existing email address
    And Click on the continue
    Then Proper warning Message Should be about duplicate email address
  @registration
  Scenario: Register without entering details into the Fields
    Given I navigated to the register page
    When I do not enter the details into the  fields
    And Click on the continue
    Then Proper warning Message Should be displayed for every mandatory field