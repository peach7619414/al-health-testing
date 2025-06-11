from selenium import webdriver
from selenium.webdriver.common.by import By

def test_appointment_booking():
    driver = webdriver.Chrome()
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