from playwright.sync_api import Page, expect

def test_smoke_test(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_text("h1", "Welcome to the-internet")

def test_forget_password_test(page: Page):
    email = ""
    expected_msg = "Your e-mail's been sent!"

    page.goto("https://the-internet.herokuapp.com/")
    page.click("a:has-text('Forgot Password')")
    page.fill("input[type=text]", email)
    page.click("button:has-text('Retrieve password')")
    expect(page).to_have_text("#content > div", expected_msg)

def test_form_authentication(page: Page):
    user_id = "tomsmith"
    password = "!"
    expected_login_msg = "You logged into a secure area!"
    expected_logout_msg = "You logged out of the secure area!"

    page.goto("https://the-internet.herokuapp.com/")
    page.click("a:has-text('Form Authentication')")
    page.fill("input[type=text]", user_id)
    page.fill("input[type=password]", password)
    page.click("button:has-text('Login')")
    expect(page).to_have_text("#flash", expected_login_msg)
    page.click("a:has-text('Logout')")
    expect(page).to_have_text("#flash", expected_logout_msg)

def test_form_authentication_bad_info(page: Page):
    user_id = "sdetAutomatiom"
    password = "!"
    expected_msg = "Your username is invalid!"

    page.goto("https://the-internet.herokuapp.com/")
    page.click("a:has-text('Form Authentication')")
    page.fill("input[type=text]", user_id)
    page.fill("input[type=password]", password)
    page.click("button:has-text('Login')")
    expect(page).to_have_text("#flash", expected_msg)