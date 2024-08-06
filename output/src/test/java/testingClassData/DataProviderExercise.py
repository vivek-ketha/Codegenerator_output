import playwright
import pytest

@pytest.fixture(scope="session")
def browser():
    with playwright.Chromium.connect() as browser:
        yield browser

def test_price_check(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    item_name = "Sauce Labs Backpack"
    price = "$29.99"
    price_element = page.locator(f"//div[contains(text(),'{item_name}')]/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']")
    assert price_element.inner_text() == price