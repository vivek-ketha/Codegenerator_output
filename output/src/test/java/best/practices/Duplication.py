import playwright
import best.practices

def test1(page):
    page.goto("http://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click(".btn_action")
    is_displayed = page.wait_for_selector("#inventory_filter_container").is_visible()
    assert is_displayed

def test2(page):
    page.goto("http://www.saucedemo.com")
    page.fill("#user-name", "problem_user")
    page.fill("#password", "secret_sauce")
    page.click(".btn_action")
    is_displayed = page.wait_for_selector("#inventory_filter_container").is_visible()
    assert is_displayed

def test3(page):
    open(page)
    type_text(page, "#user-name", "standard_user")
    type_text(page, "#password", "secret_sauce")
    click_button(page, ".btn_action")
    is_displayed = wait_until_displayed(page, "#inventory_filter_container")
    assert is_displayed

def test4(page):
    open(page)
    type_text(page, "#user-name", "problem_user")
    type_text(page, "#password", "secret_sauce")
    click_button(page, ".btn_action")
    is_displayed = wait_until_displayed(page, "#inventory_filter_container")
    assert is_displayed

def wait_until_displayed(page, locator):
    return page.wait_for_selector(locator).is_visible()

def click_button(page, locator):
    page.click(locator)

def type_text(page, locator, string):
    page.fill(locator, string)

def open(page):
    page.goto("http://www.saucedemo.com")

with best.practices.Duplication() as duplication:
    duplication.setup()
    duplication.test1()
    duplication.test2()
    duplication.test3()
    duplication.test4()
    duplication.cleanup()