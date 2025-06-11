from selenium import webdriver
from selenium.webdriver.common.by import By

def test_payment_flow():
    driver = webdriver.Chrome()
    driver.get("https://allarahealth.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    driver.find_element(By.ID, "login-button").click()
    driver.get("https://allarahealth.com/payment")
    driver.find_element(By.ID, "card-number").send_keys("4111111111111111")
    driver.find_element(By.ID, "expiry-date").send_keys("12/27")
    driver.find_element(By.ID, "cvv").send_keys("123")
    driver.find_element(By.ID, "submit-payment").click()
    assert "Payment successful" in driver.page_source
    driver.quit()