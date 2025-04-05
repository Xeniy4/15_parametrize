"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, by


def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"


@pytest.fixture(params=[(1920, 1080), (1600, 900), (375, 667), (412, 914)], ids=show_screen_size)
def browser_setting(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 500:
        yield "Desktop"
    else:
        yield "Mobile"

    browser.quit()


def test_github_desktop(browser_setting):
    if browser_setting == "Mobile":
        pytest.skip("Пропуск по причине разрешения мобильного девайса")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


def test_github_mobile(browser_setting):
    if browser_setting == "Desktop":
        pytest.skip("Пропуск по причине декстопного разрешения")
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()