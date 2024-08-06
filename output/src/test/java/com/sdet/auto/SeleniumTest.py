from playwright.sync_api import Page

def navToWebPageUnderTest(page: Page):
    page.goto("https://the-internet.herokuapp.com/")

def VerifyOnHomePage(page: Page, testAssert):
    assert page.url == "https://the-internet.herokuapp.com/"
    assert page.title == "The Internet"

def ClickForgetPassword(page: Page):
    page.click("text=Forgot Password")

def EnterEmail(page: Page, email):
    page.fill("#email", email)

def ClickRetrieveButton(page: Page):
    page.click("text=Retrieve password")

def VerifyEmailSent(page: Page, testAssert, expectedMsg):
    assert page.url == "https://the-internet.herokuapp.com/email_sent"
    assert page.title == "Email Sent"
    assert page.text_content("css=h3") == expectedMsg

def clickFormAuthentication(page: Page):
    page.click("text=Form Authentication")

def enterCredentials(page: Page, userId, password):
    page.fill("#username", userId)
    page.fill("#password", password)
    page.click("text=Login")

def verifyMessage(page: Page, testAssert, expectedMsg):
    assert page.text_content("css=div.flash.success") == expectedMsg

def clickLogoutButton(page: Page):
    page.click("text=Logout")

def basicAccessibilityCheck(page: Page, testAssert):
    pass