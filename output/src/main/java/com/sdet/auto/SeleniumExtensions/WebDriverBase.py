from playwright.sync_api import ChromeOptions, FirefoxOptions, RemoteWebDriver, sync_playwright

def get_webdriver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("disable-infobars")
        driver = RemoteWebDriver(executable_path="src/main/resources/chromedriver", options=options)
        driver.manage().delete_all_cookies()

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("disable-infobars")
        driver = RemoteWebDriver(executable_path="src/main/resources/geckodriver", options=options)
        driver.manage().window().maximize()

    elif browser == "seleniumGrid":
        grid_url = "http://y75EbcWLcnPNI0p8sZBQTcTUGj5PCOl0:LhvNjhomu4Z3Ue2d3tTMwDx3MtJe7V5I@SESYNPZ6.gridlastic.com:80/wd/hub"
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("disable-infobars")
        capabilities = DesiredCapabilities.chrome()
        capabilities.set_capability(ChromeOptions.CAPABILITY, options)
        driver = RemoteWebDriver(command_executor=grid_url, desired_capabilities=capabilities)
        driver.manage().window().maximize()

    else:
        raise RuntimeError(f"Browser type {browser} not found, please add additional code for this desired WebDriver type.")

    return driver