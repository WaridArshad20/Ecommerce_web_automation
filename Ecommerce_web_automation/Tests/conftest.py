import pytest
from selenium import webdriver
from utilities.utilities import load_config, load_test_data


@pytest.fixture(scope="session")
def config():
    """Load and return the configuration data."""
    return load_config()


@pytest.fixture(scope="session")
def test_data():
    """Load and return the test data."""
    return load_test_data()


@pytest.fixture(scope="session")
def browser(config):
    """Initialize the WebDriver based on the browser type in config."""
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{config['browser']}' is not supported.")

    driver.implicitly_wait(config['timeouts']['implicit_wait'])
    driver.set_page_load_timeout(config['timeouts']['page_load_timeout'])
    yield driver
    driver.quit()
