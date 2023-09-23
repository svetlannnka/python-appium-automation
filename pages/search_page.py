from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from pages.base_page import Page


class SearchPage(Page):
    SEARCH_FIELD = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia:id/page_list_item_title')

    def search_wiki(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.wait_for_element_appear(*self.SEARCH_RESULT)

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.SEARCH_RESULT)