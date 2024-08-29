from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """Home page POM."""
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def search(self, text):
        """Search for a term."""
        self.enter_text(self.SEARCH_BOX, text)
        self.click(self.SEARCH_BUTTON)
