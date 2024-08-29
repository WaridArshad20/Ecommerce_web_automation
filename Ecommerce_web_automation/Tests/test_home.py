from pages.home_page import HomePage

def test_google_search(browser, config, test_data):
    """A simple test case to search on Google using test data."""
    home_page = HomePage(browser)
    browser.get(config['base_url'])
    home_page.search(test_data['search_term'])
    assert test_data['search_term'] in browser.title
