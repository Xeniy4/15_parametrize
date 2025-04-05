"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, by


def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1280, 720)], ids=show_screen_size)
def desktop_browser_setting(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[(412, 914), (430, 932), (375, 667)], ids=show_screen_size)
def mobile_browser_setting(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_github_desktop(desktop_browser_setting):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


def test_github_mobile(mobile_browser_setting):
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()