from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH = (By.XPATH, "//*[@text='Search Wikipedia']")

    def click_search_wiki(self):
        self.click(*self.SEARCH)