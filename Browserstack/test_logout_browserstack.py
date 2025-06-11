import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout_browserstack():
    desired_cap = {
        'browser': 'Safari',
        'os': 'OS X',
        'os_version': 'Ventura',
        'name': 'Logout Test',
        'build': 'Allara BrowserStack Build'
    }
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_KEY')}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    driver.get("https://allarahealth.com/dashboard")
    driver.find_element(By.ID, "logout-link").click()
    assert "Login" in driver.page_source
    driver.quit()