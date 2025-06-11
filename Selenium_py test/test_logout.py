from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://allarahealth.com/dashboard")
    driver.find_element(By.ID, "logout-link").click()
    assert "Login" in driver.page_source
    driver.quit()