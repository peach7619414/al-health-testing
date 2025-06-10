import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_free_quote_missing_name():
    driver = webdriver.Chrome()
    driver.get("https://homepro.herokuapp.com/quote.php")
    driver.find_element(By.NAME, "email").send_keys("john@example.com")
    driver.find_element(By.NAME, "phone").send_keys("123-456-7890")
    driver.find_element(By.NAME, "description").send_keys("Need a quote")
    driver.find_element(By.ID, "submit_button").click()
    assert "Error-001" in driver.page_source
    driver.quit()