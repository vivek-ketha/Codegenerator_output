from playwright.sync_api import Playwright, Locator

playwright = Playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://www.saucedemo.com/")
locator = page.locator("#user-name")
page.wait_for_selector("#user-name")
browser.close()