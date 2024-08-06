from playwright.sync_api import Page

class PersonalInfoPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_out_personal_information(self):
        self.page.fill("#FAKE LOCATOR", "firstName")
        self.page.fill("#FAKE LOCATOR", "lastName")
        self.page.fill("#FAKE LOCATOR", "zipCode")