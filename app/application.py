from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.welcome_page import WelcomePage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.welcome_page = WelcomePage(self.driver)
