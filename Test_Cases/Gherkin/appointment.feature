Feature: Appointment Booking

  Scenario: Book an appointment successfully
    Given I am logged in
    When I select a provider and time
    And I confirm the appointment
    Then I should see a confirmation message

  Scenario: Book an already booked time slot
    Given I already have an appointment
    When I select the same slot again
    And I confirm the appointment
    Then I should see a conflict error