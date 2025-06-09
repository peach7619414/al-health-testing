
def test_appointment_booking():
    # Setup
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("https://allarahealth.com/login")

    # Log in
    driver.find_element(By.NAME, "username").send_keys("jane.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
    driver.find_element(By.NAME, "login_button").click()

    # Navigate to appointment booking page
    driver.get("https://allarahealth.com/book-appointment")
    
    # Select professional and time slot
    driver.find_element(By.NAME, "professional").click()
    driver.find_element(By.NAME, "time_slot").click()
    
    # Fill details and book
    driver.find_element(By.NAME, "details").send_keys("General checkup")
    driver.find_element(By.NAME, "book_button").click()

    # Wait for confirmation
    time.sleep(5)

    # Verify results
    assert "Appointment Confirmed" in driver.page_source
    driver.quit()

# Run the test
test_appointment_booking()
