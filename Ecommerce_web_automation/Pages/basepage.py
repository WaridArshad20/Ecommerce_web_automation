from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Find a single element on the page."""
        return self.driver.find_element(*locator)

    def click(self, locator):
        """Click an element on the page."""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Enter text into a field."""
        self.find_element(locator).send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
