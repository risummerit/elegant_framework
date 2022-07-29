from pytest import fixture
from selenium import webdriver


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome('/Users/rimmagizzatova/Projects_Ri/udemy_elegant_pytest/chromedriver')
    yield browser

    # Teardown
    browser.quit()
