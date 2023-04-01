from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/Users/svetlanalevinsohn/JobEasy/python-appium-automation/mobile_app/wikipedia.apk"
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)

# Click Skip
driver.find_element(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

# Click search icon
driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="Search Wikipedia"]').click()

# Search for Python (Programming language)
driver.find_element(By.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (Programming language)')

# Verify text is correct
expected_text = 'Python (programming language)'
actual_text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
assert actual_text == expected_text, f'Expected {expected_text} but got actual {actual_text}'

print('Test case passed')
driver.quit()

##  10 min break
