from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def mobile_init(context, test_name):
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
        "app": "mobile_app/wikipedia.apk"
    }

    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
