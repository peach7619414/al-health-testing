
def test_user_login():
    # Setup
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("https://allarahealth.com/login")

    # Test steps
    driver.find_element(By.NAME, "username").send_keys("jane.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
    driver.find_element(By.NAME, "login_button").click()

    # Verify results
    assert "Welcome, Jane Doe" in driver.page_source
    driver.quit()

# Run the test
test_user_login()
