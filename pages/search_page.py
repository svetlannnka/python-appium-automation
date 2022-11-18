from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchPage(Page):
    SEARCH_INPUT = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')

    def input_search_query(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def verify_search_results(self, expected_text):
        self.verify_element_text(expected_text, *self.SEARCH_RESULT)