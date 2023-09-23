from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.welcome_page import WelcomePage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.search_page = SearchPage(driver)
        self.welcome_page = WelcomePage(driver)