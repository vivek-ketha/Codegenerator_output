from playwright.sync_api import Page

class ProductDataProvider:
    @staticmethod
    def provide_user_data():
        return [
            ("Sauce Labs Backpack", "$29.99"),
            ("Sauce Labs Bike Light", "$9.99"),
            ("Sauce Labs Bolt T-Shirt", "$15.99"),
            ("Sauce Labs Fleece Jacket", "$49.99"),
            ("Sauce Labs Onesie", "$7.99"),
            ("Test.allTheThings() T-Shirt (Red)", "$15.99")
        ]