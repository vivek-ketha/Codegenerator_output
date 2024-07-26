
from playwright.sync_api import Page, expect

def basic_accessibility_check(page: Page):
    script_url = "path/to/axe.min.js"
    response_json = page.evaluate(
        """
        const axe = require('axe-core');
        return axe.run(document, {
            scriptUrl: '""" + script_url + """'
        });
        """
    )
    violations = response_json["violations"]

    if len(violations) == 0:
        print("PASS: basicAccessibilityCheck | No violations found.")
    else:
        print("FAIL: " + IoLibrary.getTestName() + " " + AXE.report(violations))