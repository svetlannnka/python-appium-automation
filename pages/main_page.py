from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH_ICON = (By.XPATH, '//android.widget.ImageView[@content-desc="Search Wikipedia"]')
    SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_src_text')

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def input_search_phrase(self):
        self.input_text('Python (Programming language)', *self.SEARCH_FIELD)