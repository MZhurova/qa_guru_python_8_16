"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from selene import have
from selene import browser
import pytest

desktop = pytest.mark.parametrize("browser_window", ['Desktop'], indirect=True)
mobile = pytest.mark.parametrize("browser_window", ['Mobile'], indirect=True)


@pytest.fixture(params=['Desktop', 'Mobile'])
def browser_window(request):
    if request.param == "Desktop":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    if request.param == "Mobile":
        browser.config.window_width = 375
        browser.config.window_height = 812


@desktop
def test_github_desktop(browser_window):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@mobile
def test_github_mobile(browser_window):
    browser.open("https://github.com")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
