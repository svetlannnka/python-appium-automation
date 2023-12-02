from pages.base_page import Page
from pages.explore_page import ExplorePage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.explore_page = ExplorePage(driver)
        self.ob_page = OnboardingPage(driver)
        self.search_page = SearchPage(driver)
