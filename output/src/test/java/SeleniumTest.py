from playwright.sync_api import Playwright, sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def safari_test():
    options = Options()
    options.binary_location = "/Applications/Safari.app/Contents/MacOS/Safari"
    driver = webdriver.Safari(options=options)
    driver.get("https://the-internet.herokuapp.com/")
    driver.quit()

def cypress_test():
    options = Options()
    options.binary_location = "/Applications/Safari.app/Contents/MacOS/Safari"
    driver = webdriver.Safari(options=options)
    driver.get("https://example.cypress.io/")
    driver.quit()

def shopping_cart_test():
    options = Options()
    options.binary_location = "/Applications/Safari.app/Contents/MacOS/Safari"
    driver = webdriver.Safari(options=options)
    driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    driver.quit()

with sync_playwright() as playwright:
    safari_test()
    cypress_test()
    shopping_cart_test()