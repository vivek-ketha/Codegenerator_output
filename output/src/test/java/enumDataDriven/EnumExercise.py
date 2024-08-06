from enum import Enum
from playwright.sync_api import Page, Playwright

class SortValue(Enum):
    PRICE_LOW_TO_HIGH = "lohi"
    PRICE_HIGH_TO_LOW = "hilo"
    NAME_A_TO_Z = "az"
    NAME_Z_TO_A = "za"

def test_sorting(page: Page, playwright: Playwright, value: SortValue):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "")
    page.click("#login-button")
    sort_dropdown = page.select_option(".product_sort_container", value=value.value)