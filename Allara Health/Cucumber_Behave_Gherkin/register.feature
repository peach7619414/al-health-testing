
Feature: User Registration

  Scenario: A new user registers successfully
    Given I am on the Allara Health registration page
    When I fill in the registration form with valid details
    And I submit the form
    Then I should see a confirmation message
    And I should receive a confirmation email
