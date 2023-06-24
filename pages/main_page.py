from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class MainPage(Page):
    SEARCH_ICON = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Search Wikipedia']")

    def click_search(self):
        self.click(*self.SEARCH_ICON)