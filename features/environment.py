from appium import webdriver
from appium.options.android import UiAutomator2Options

from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def app_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """

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

    context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # Pass scenario.name to init() for browserstack config:
    app_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
