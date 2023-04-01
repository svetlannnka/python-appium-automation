from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')

    def verify_search_result(self):
        expected_text = 'Python (programming language)'
        self.verify_text(expected_text, *self.SEARCH_RESULT)