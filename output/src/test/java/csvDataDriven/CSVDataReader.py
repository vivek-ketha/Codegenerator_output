import csv
import unittest

from playwright.sync_api import Page, Playwright

class CSVDataReader(unittest.TestCase):
    def setUp(self):
        self.playwright = Playwright.install()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.page.goto("https://www.saucedemo.com/")

    def tearDown(self):
        self.browser.close()

    def test_login(self):
        with open("Users.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                username, password = row
                self.page.fill("#user-name", username)
                self.page.fill("#password", password)
                self.page.click("#login-button")
                self.assertTrue(self.page.is_visible(".title"))
                self.page.goto("https://www.saucedemo.com/")