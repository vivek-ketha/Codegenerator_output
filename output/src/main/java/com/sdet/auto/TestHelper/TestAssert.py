from playwright.sync_api import Page

class TestAssert:
    def __init__(self):
        self.pass = True

    def get_pass(self):
        return self.pass

    def set_pass(self, pass):
        if self.pass:
            self.pass = pass