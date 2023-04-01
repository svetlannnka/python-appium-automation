from selenium.webdriver.common.by import By

from pages.base_page import Page


class OnboardingPage(Page):
    SKIP_BTN = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def click_skip(self):
        self.find_element(*self.SKIP_BTN).click()

