
# BrowserStack configuration for cross-browser testing
desired_caps = {
    'browser': 'Chrome',
    'browser_version': 'latest',
    'os': 'Windows',
    'os_version': '10',
    'name': 'Appointment Booking Test',
    'build': 'Test Build 1.0',
}

driver = webdriver.Remote(
    command_executor='https://<username>:<access_key>@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_caps
)
