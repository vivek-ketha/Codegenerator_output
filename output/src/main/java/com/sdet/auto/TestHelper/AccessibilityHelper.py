
from playwright.sync_api import Page
from axe_playwright import AxePlaywright

def basic_accessibility_check(page: Page):
    axe_plugin = AxePlaywright(page)
    results = axe_plugin.analyze()

    if len(results["violations"]) == 0:
        print("PASS: basicAccessibilityCheck | No violations found.")
    else:
        axe_plugin.write_results("FAIL: " + IoLibrary.getTestName(), results)
        print("FAIL: " + IoLibrary.getTestName() + " " + axe_plugin.report(results["violations"]))