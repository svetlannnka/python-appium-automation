from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def mobile_driver_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    desired_capabilities = {
        "platformName": "Android",
        "automationName": 'uiautomator2',
        "platformVersion": "12",
        "deviceName": "Android Emulator",
        "appActivity": "org.wikipedia.main.MainActivity",
        "appPackage": "org.wikipedia",
        "app": "/Users/svetlanalevinsohn/JobEasy/python-appium-automation/mobile_app/wikipedia.apk"
    }

    context.driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=desired_capabilities)

    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
