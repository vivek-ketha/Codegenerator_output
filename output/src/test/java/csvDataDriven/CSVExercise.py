import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # skip header row
        return list(reader)

def test_login(page):
    for item_name, price in read_csv_file('Prices.csv'):
        price_element = page.locator(f"//div[contains(text(),'{item_name}')]/ancestor::div[@class='inventory_item_description']//div[@class='inventory_item_price']")
        assert price_element.inner_text() == price