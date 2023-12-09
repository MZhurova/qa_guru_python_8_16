"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
from selene import have
from selene import browser
import pytest


@pytest.fixture(params=[(1920, 1080, 'Desktop'), (375, 812, 'Mobile'), (2560, 1440, 'Desktop'), (720, 1280, 'Mobile')])
def browser_window(request):
    if request.param[2] == 'Desktop':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]

    if request.param[2] == 'Mobile':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]


def test_github_desktop(browser_window):
    if browser_window == 'Mobile':
        pytest.skip('Пропускаем тест потому что соотношение сторон мобильное')
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_window):
    if browser_window == 'Desktop':
        pytest.skip('Пропускаем тест потому что соотношение сторон десктопное')
    browser.open("https://github.com")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
