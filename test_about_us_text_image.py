import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_about_us_image_and_text():
    driver = webdriver.Chrome()
    driver.get("https://homepro.herokuapp.com/about.php")
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Putting people first')]").is_displayed()
    assert driver.find_element(By.XPATH, "//img[contains(@src, 'about-us.jpg')]").is_displayed()
    driver.quit()