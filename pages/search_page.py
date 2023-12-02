from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page


class SearchPage(Page):
    SEARCH_FIELD = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia:id/page_list_item_title')

    def input_search_text(self, search_text):
        self.input(search_text, *self.SEARCH_FIELD)

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)
