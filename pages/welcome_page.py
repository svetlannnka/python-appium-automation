from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class WelcomePage(Page):
    SKIP_BTN = (AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def skip_onboarding(self):
        self.click(*self.SKIP_BTN)