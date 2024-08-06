from playwright.sync_api import Page, Playwright

def test_synchronization(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.wait_for_selector("#finish")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.wait_for_selector("#start")
    page.click("#start button")
    page.wait_for_selector("#finish")