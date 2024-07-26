
from playwright.sync_api import Page

class EmailSentPage:
    txtMessage = "#content"

    def __init__(self, page: Page):
        self.page = page

    def verify_email_sent(self, test_assert, expected_msg):
        actual_msg = self.page.get_by_selector(self.txtMessage).text_content()
        test_assert.set_pass(LoggingLibrary.compare_result(actual_msg, expected_msg))