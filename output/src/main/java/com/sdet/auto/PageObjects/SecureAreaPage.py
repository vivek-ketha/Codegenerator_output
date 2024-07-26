
from playwright.sync_api import Page

def verify_message(page: Page, expected_msg: str) -> bool:
    lbl_message = page.locator("#flash")
    return lbl_message.inner_text().contains(expected_msg)

def click_logout_button(page: Page) -> None:
    btn_logout = page.locator(".icon-2x.icon-signout")
    btn_logout.click()