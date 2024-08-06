from playwright.sync_api import Page

def get_element_by_selector(page: Page, css_selector: str) -> Page:
    return page.wait_for_selector(css_selector)

def get_element_by_selector_with_timeout(page: Page, css_selector: str, wait_seconds: int) -> Page:
    return page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

def selenium_exception_handler(ex: Exception) -> None:
    print(f"Selenium Exception Handler Caught Exception: [{ex}]")
    screenshot()

def screenshot(page: Page) -> None:
    try:
        print("Attempting Selenium Screenshot ...")
        screenshot_dir = "/path/to/screenshots"
        test_name = f"{page.context.options['name']}_{page.context.options['unique_identifier']}.png"
        screenshot = page.screenshot()
        with open(f"{screenshot_dir}/{test_name}", "wb") as f:
            f.write(screenshot)
        print(f"Browser Screenshot Save Location: {screenshot_dir}/{test_name}")
    except Exception as ex:
        print(f"Failed to take screenshot: {ex}")