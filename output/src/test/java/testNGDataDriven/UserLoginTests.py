from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "")
    page.click("#login-button")
    expect(page).to_have_text(".title", "Products")