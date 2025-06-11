Feature: Cancel Appointment

  Scenario: Cancel a future appointment
    Given I have an appointment booked
    When I go to the appointment and click cancel
    Then I should see a cancellation confirmation