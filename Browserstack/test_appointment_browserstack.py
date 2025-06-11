import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_appointment_browserstack():
    desired_cap = {
        'browser': 'Chrome',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Appointment Booking Test',
        'build': 'Allara BrowserStack Build'
    }
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_KEY')}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    driver.get("https://allarahealth.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    driver.find_element(By.ID, "login-button").click()
    driver.get("https://allarahealth.com/appointments")
    driver.find_element(By.ID, "provider-dropdown").click()
    driver.find_element(By.XPATH, "//option[text()='Dr. Jane Smith']").click()
    driver.find_element(By.ID, "confirm-appointment").click()
    assert "Appointment confirmed" in driver.page_source
    driver.quit()