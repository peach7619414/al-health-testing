Feature: Change Password

  Scenario: Update password with valid current password
    Given I am logged in
    When I go to change password
    And I enter the correct current password and a new password
    Then I should see a success message

  Scenario: Update password with incorrect current password
    Given I am logged in
    When I enter an incorrect current password
    Then I should see an error message