Feature: Login Functionality

  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter valid email and password
    And I click the login button
    Then I should see the dashboard

  Scenario: Login with invalid password
    Given I am on the login page
    When I enter valid email and wrong password
    And I click the login button
    Then I should see an error message