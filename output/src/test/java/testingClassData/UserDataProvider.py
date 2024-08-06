from playwright.sync_api import Page

class UserDataProvider:
    @staticmethod
    def provide_user_data():
        return [
            {"username": "standard_user", "password": ""},
            {"username": "performance_glitch_user", "password": ""},
            {"username": "problem_user", "password": ""},
        ]

def test_login(page: Page, user_data):
    username = user_data["username"]
    password = user_data["password"]
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("text=LOGIN")
    assert page.url == "https://www.saucedemo.com/inventory.html"
