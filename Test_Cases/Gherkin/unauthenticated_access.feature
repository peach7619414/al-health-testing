Feature: Access Control

  Scenario: Unauthenticated user tries to access protected page
    Given I am not logged in
    When I try to open the profile page URL
    Then I should be redirected to the login page