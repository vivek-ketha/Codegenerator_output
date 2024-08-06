from playwright.sync_api import Page

class EmailSentPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def txt_message(self):
        return self.page.locator("#content")

    def verify_email_sent(self, expected_msg):
        actual_msg = self.txt_message.text_content()
        assert actual_msg == expected_msg