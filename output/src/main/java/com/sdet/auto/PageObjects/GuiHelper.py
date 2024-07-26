
from playwright.sync_api import Playwright, sync_playwright

def open_web_browser():
    with sync_playwright() as playwright:
        global browser
        browser = playwright.chromium.launch()
        global page
        page = browser.new_page()

def open_web_browser_with_chrome(chrome):
    with sync_playwright() as playwright:
        global browser
        browser = playwright.chromium.launch(executable_path=chrome)
        global page
        page = browser.new_page()

def close_web_browser():
    browser.close()