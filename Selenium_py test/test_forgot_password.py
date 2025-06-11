from selenium import webdriver
from selenium.webdriver.common.by import By

def test_forgot_password():
    driver = webdriver.Chrome()
    driver.get("https://allarahealth.com/forgot-password")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "reset-button").click()
    assert "Reset link sent" in driver.page_source
    driver.quit()