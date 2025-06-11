from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register():
    driver = webdriver.Chrome()
    driver.get("https://allarahealth.com/register")
    driver.find_element(By.ID, "email").send_keys("newuser@example.com")
    driver.find_element(By.ID, "password").send_keys("Test1234!")
    driver.find_element(By.ID, "confirm-password").send_keys("Test1234!")
    driver.find_element(By.ID, "register-button").click()
    assert "Welcome" in driver.page_source
    driver.quit()