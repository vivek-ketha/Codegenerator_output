
from playwright.sync_api import Page

class EmailSentPage:
    txt_message = "#content"

    @staticmethod
    def verify_email_sent(page: Page, test_assert, expected_msg):
        test_assert.set_pass(page.locator(EmailSentPage.txt_message).text_content() == expected_msg)