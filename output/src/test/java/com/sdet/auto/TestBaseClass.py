import pytest
from playwright.sync_api import Page

class TestBaseClass:
    def __init__(self, page: Page):
        self.page = page

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(self):
        self.config_settings = ConfigSettings()
        self.config_settings.get_config_settings()

    def setup(self):
        self.test_assert = TestAssert()

    def teardown(self):
        assert self.test_assert.get_pass()