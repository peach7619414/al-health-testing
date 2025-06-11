Feature: User Registration

  Scenario: Register with valid data
    Given I am on the registration page
    When I enter valid user details
    And I click register
    Then I should be redirected to the welcome page

  Scenario: Register with missing email
    Given I am on the registration page
    When I leave the email field empty
    And I click register
    Then I should see a validation error