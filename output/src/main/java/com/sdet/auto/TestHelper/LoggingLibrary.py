from playwright.sync_api import Page

def compare_result(page: Page, actual: str, expected: str) -> bool:
    if actual == expected:
        page.log.info(f"PASS: Actual({actual}) | Expected({expected})")
        return True
    else:
        page.log.error(f"FAIL: Actual({actual}) | Expected({expected})")
        return False

def compare_result_contains(page: Page, actual: str, expected: str) -> bool:
    if expected in actual:
        page.log.info(f"PASS: Actual({actual}) | ExpectedToContain({expected})")
        return True
    else:
        page.log.error(f"FAIL: Actual({actual}) | ExpectedToContain({expected})")
        return False