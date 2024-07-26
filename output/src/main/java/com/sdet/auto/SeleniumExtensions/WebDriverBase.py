
import sys
from pathlib import Path
sys.path.append(str(Path.cwd().parent / "src"))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.remote_webdriver import RemoteWebDriver
from typing import Union

def get_webdriver(browser: str) -> Union[WebDriver, RemoteWebDriver]:
    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=options)
        driver.delete_all_cookies()

    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif browser == "seleniumGrid":
        grid_url = "http://y75EbcWLcnPNI0p8sZBQTcTUGj5PCOl0:LhvNjhomu4Z3Ue2d3tTMwDx3MtJe7V5I@SESYNPZ6.gridlastic.com:80/wd/hub"
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("disable-infobars")
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities["chromeOptions"] = options.__dict__
        driver = RemoteWebDriver(command_executor=grid_url, desired_capabilities=capabilities)
        driver.maximize_window()

    else:
        raise RuntimeError(f"Browser type {browser} not found")

    return driver

def get_webdriver_from_chrome(chrome: WebDriver) -> None:
    driver = chrome
    driver.delete_all_cookies()
    driver.maximize_window()