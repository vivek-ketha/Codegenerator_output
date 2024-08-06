from playwright.sync_api import Page
from axe_playwright import axe_playwright

def basic_accessibility_check(page: Page):
    results = axe_playwright(page).analyze()
    if results["violations"]:
        print("FAIL: basic_accessibility_check | Violations found.")
        print(results["violations"])
    else:
        print("PASS: basic_accessibility_check | No violations found.")