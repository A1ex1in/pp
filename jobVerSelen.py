import time
from selenium import webdriver
from openpyxl import Workbook
driver = webdriver.Chrome()
driver.get('https://iotvega.com/product')
time.sleep(15)
wb = Workbook()
ws = wb.active
product_elements = driver.find_elements('css selector', '.product-name')
price_elements = driver.find_elements('css selector', '.price_item')
for product, price in zip(product_elements, price_elements):
    product_name = product.text
    product_price = price.text
    ws.append([product_name, product_price])
wb.save('products.xlsx')
driver.quit()