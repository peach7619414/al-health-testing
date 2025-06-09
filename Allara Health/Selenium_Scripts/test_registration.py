
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration():
    # Setup
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("https://allarahealth.com/register")

    # Test steps
    driver.find_element(By.NAME, "full_name").send_keys("Jane Doe")
    driver.find_element(By.NAME, "email").send_keys("jane.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
    driver.find_element(By.NAME, "dob").send_keys("01/01/1985")
    driver.find_element(By.NAME, "register_button").click()

    # Wait for confirmation
    time.sleep(5)  # Waiting for confirmation page to load

    # Verify results
    assert "Confirmation" in driver.page_source
    driver.quit()

# Run the test
test_registration()
