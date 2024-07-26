
from playwright.sync_api import Page, sync_playwright

def download_file_from_url(url: str, destination: str):
    with sync_playwright() as playwright:
        with playwright.chromium.launch() as browser:
            page = browser.new_page()
            page.goto(url)
            page.download(destination)