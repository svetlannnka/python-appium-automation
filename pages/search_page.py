from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class SearchPage(Page):
    SEARCH_INPUT = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia:id/page_list_item_title')

    def search_on_wiki(self, search_phrase):
        self.input_text(search_phrase, *self.SEARCH_INPUT)

    def verify_search_result(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULT)
