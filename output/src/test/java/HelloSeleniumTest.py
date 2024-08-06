import playwright

def test_first_test():
    with playwright.sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        browser.close()