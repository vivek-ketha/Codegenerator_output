  from playwright.sync_api import Page

  class HomePage(Page):
      def __init__(self, page: Page):
          self.page = page

      txt_header = ".heading"
      link_forget_password = "[href='/forgot_password']"
      link_form_authentication = "[href='/login']"

      def click_forget_password(self):
          self.page.locator(self.link_forget_password).click()

      def click_form_authentication(self):
          self.page.locator(self.link_form_authentication).click()

      def verify_on_home_page(self, test_assert):
          header_text = self.page.locator(self.txt_header).text_content()
          test_assert.set_pass(LoggingLibrary.compare_result(header_text, "Welcome to the-internet"))