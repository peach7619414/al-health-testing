from selenium import webdriver
from selenium.webdriver.common.by import By

def test_profile_update():
    driver = webdriver.Chrome()
    driver.get("https://allarahealth.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    driver.find_element(By.ID, "login-button").click()
    driver.get("https://allarahealth.com/profile")
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("Updated User")
    driver.find_element(By.ID, "save-button").click()
    assert "Profile updated" in driver.page_source
    driver.quit()