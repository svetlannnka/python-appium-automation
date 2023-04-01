from pages.onboarding_page import OnboardingPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.onboarding_page = OnboardingPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultsPage(self.driver)
