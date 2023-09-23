from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from time import sleep

desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/Users/svetlanalevinsohn/JobEasy/python-appium-automation/mobile_app/wikipedia.apk"
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

# Click Skip
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

# Click on search icon
driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Search Wikipedia']").click()

# Search for Python programming language
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python programming language')
sleep(5)

search_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text
expected_result = 'Python (programming language)'
assert search_result == expected_result, f'Expected {expected_result} but got {search_result}'

driver.quit()
