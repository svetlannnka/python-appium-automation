from app.application import Application

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def driver_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "Android Emulator",
        "appActivity": "org.wikipedia.main.MainActivity",
        "appPackage": "org.wikipedia",
        "app": "/Users/svetlanalevinsohn/JobEasy/python-appium-automation/mobile_app/wikipedia.apk"
    }
    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=desired_capabilities)

    # BROWSER STACK config:
    # desired_capabilities = {
    #     "platformName": "Android",
    #     "app": "bs://c4ad6f96d57d004c2c94745c11ab10aa163f76ed",
    #     "deviceName": "Google Pixel 3",
    #     "os_version": "10.0",
    #     'bstack:options': {
    #         'userName': '',
    #         "sessionName": test_name,
    #         'accessKey': ''
    #     }
    # }
    # remote_url = 'http://hub-cloud.browserstack.com/wd/hub'
    #
    # context.driver = webdriver.Remote(command_executor=remote_url,
    #                           desired_capabilities=desired_capabilities)
    #

    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.quit()
