
from playwright.sync_api import Page, Browser
from playwright import sync_api

def get_element_by_selector(page: Page, css_selector: str) -> sync_api.ElementHandle:
    return page.wait_for_selector(css_selector)

def get_element_by_selector(page: Page, css_selector: str, wait_seconds: int) -> sync_api.ElementHandle:
    return page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

def wait_for_element(page: Page, locator: str, wait_seconds: int) -> sync_api.ElementHandle:
    return page.wait_for_selector(locator, timeout=wait_seconds * 1000)

def selenium_exception_handler(page: Page, ex: Exception) -> None:
    exception_name = ex.__class__.__name__
    print(f"Selenium Exception Handler Caught Exception: [{exception_name}]")
    screenshot(page)
    print("End of Selenium Exception Handler")

def screenshot(page: Page) -> None:
    print("Attempting Selenium Screenshot...")
    test_name = f"{page.context.options['testName']}_{page.context.options['uniqueIdentifier']}.png"
    screenshot = page.screenshot()
    with open(f"screenshots/{test_name}", "wb") as f:
        f.write(screenshot)
    print(f"Browser Screenshot Save Location: {test_name}")