import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("item_name, price", [
    ("Sauce Labs Backpack", "$29.99"),
    ("Sauce Labs Bike Light", "$9.99"),
    ("Sauce Labs Bolt T-Shirt", "$15.99"),
    ("Sauce Labs Fleece Jacket", "$49.99"),
    ("Sauce Labs Onesie", "$7.99"),
    ("Test.allTheThings() T-Shirt (Red)", "$15.99")
])
def test_price_check(driver, item_name, price):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    x_path = f"//div[contains(text(),'{item_name}')]/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']"
    price_element = driver.find_element(By.XPATH, x_path)
    assert price_element.text == price