
import os

def get_web_url():
    return web_url

def set_web_url(url):
    global web_url
    web_url = url

def get_web_browser():
    return web_browser

def set_web_browser(browser):
    global web_browser
    web_browser = browser

web_url = None
web_browser = None

def get_config_settings():
    config_file = "config.properties"
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    with open(config_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith("webUrl"):
            set_web_url(line.split("=")[1].strip())
        elif line.startswith("webBrowser"):
            set_web_browser(line.split("=")[1].strip())

    print("Test Config Settings")
    print(f"WebUrl: {get_web_url()}")
    print(f"WebBrowser: {get_web_browser()}")
    print("Test Config Settings End")

if __name__ == "__main__":
    get_config_settings()