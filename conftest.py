import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose languages")

@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = None
    browser = webdriver.Chrome(options=options)
    #browser = webdriver.Chrome()
    #browser.get(f'http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/')
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()