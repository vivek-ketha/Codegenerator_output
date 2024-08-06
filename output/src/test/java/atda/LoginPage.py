from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def open(self):
        await self.page.goto("http://www.saucedemo.com")

    async def is_loaded(self):
        return await expect(self.page).to_be_visible("#user-name").is_visible()

    async def login(self, user_name, password):
        await self.page.fill("#user-name", user_name)
        await self.page.fill("#password", password)
        await self.page.click(".btn_action")