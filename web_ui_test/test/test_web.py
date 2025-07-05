import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

scenarios('../features/web.feature')


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    service = Service("C:/Drivers/chromedriver-win64/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given('the DuckDuckGo home page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)
    return browser


@when(parsers.parse('the user searches for "{text}"'))
def search_phrase_inline(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)


@when(parsers.re(r'the user searches for the phrase """(?P<text>.+)"""'))
def search_phrase_multiline(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)


@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = f"//*[@data-testid='result']//*[contains(text(), '{phrase}')]"
    results = browser.find_elements(By.XPATH, xpath)
    assert len(results) > 0, f"No result contains phrase '{phrase}'."


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    results = browser.find_elements(By.CSS_SELECTOR, '[data-testid="result"]')
    assert len(results) > 0, "No search results found."
    search_input = browser.find_element(By.NAME, 'q')
    assert search_input.get_attribute('value') == phrase

