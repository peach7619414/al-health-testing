
def test_payment_system():
    # Setup
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("https://allarahealth.com/login")

    # Log in
    driver.find_element(By.NAME, "username").send_keys("jane.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
    driver.find_element(By.NAME, "login_button").click()

    # Navigate to payment page
    driver.get("https://allarahealth.com/payment")

    # Select payment method and enter details
    driver.find_element(By.NAME, "payment_method").send_keys("Credit Card")
    driver.find_element(By.NAME, "credit_card_number").send_keys("4111111111111111")
    driver.find_element(By.NAME, "expiry_date").send_keys("12/25")
    driver.find_element(By.NAME, "submit_payment").click()

    # Verify payment confirmation
    assert "Payment Successful" in driver.page_source
    driver.quit()

# Run the test
test_payment_system()
