
from playwright.sync_api import Page, expect

def get_element_by_selector(page: Page, css_selector: str, wait_seconds: int = 10) -> str:
    return page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

def selenium_exception_handler(ex: Exception) -> None:
    exception_name = ex.message
    print(f"WebDriver Exception Handler Caught Exception: [{exception_name}]")
    screenshot()
    print(" ")

def screenshot(page: Page) -> None:
    test_name = f"{page.context.options['testName']}_{page.context.options['uniqueIdentifier']}.png"
    screenshot_dir = f"{page.context.options['dirPath']}/target/outputs/screenshots/"

    try:
        print("Attempting Selenium Screenshot ...")
        page.wait_for_timeout(1000)
        screenshot = page.screenshot()
        with open(screenshot_dir + test_name, "wb") as f:
            f.write(screenshot)
        print(f"Browser Screenshot Save Location: {screenshot_dir + test_name}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")