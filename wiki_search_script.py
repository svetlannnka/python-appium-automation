from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "mobile_app/wikipedia.apk"
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)

# click Skip
driver.find_element(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

# click Search Wiki
driver.find_element(By.XPATH, "//*[@text='Search Wikipedia']").click()

# input search text
driver.find_element(By.ID, 'org.wikipedia:id/search_src_text').send_keys('Python')

# Verification:
actual_result = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
expected_result = 'Python'

assert actual_result == expected_result, f'Error! Expected {expected_result} did not match {actual_result}'

driver.quit()