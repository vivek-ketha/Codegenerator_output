from enum import Enum
import pytest
from playwright.sync_api import Page, sync_playwright


class User(Enum):
    STANDARD ='standard_user'
    LOCKED = 'locked_out_user'
    PROBLEMS = 'problem_user'
    PERFORMANCE = 'performance_glitch_user'


def get_driver():
    with sync_playwright() as playwright:
        return playwright.chromium.launch()


@pytest.fixture(scope='session')
def driver():
    return get_driver()


@pytest.fixture(scope='function')
def page(driver):
    page = driver.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


def test_login(page, user):
    page.fill("#user-name", user.value)
    page.fill("#password", "")
    page.click("#login-button")
    assert page.is_visible(".title")