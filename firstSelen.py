from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
driver = webdriver.Edge()
driver.get('https://iotvega.com/product')
source_data = driver.page_source
soup = BeautifulSoup(source_data, features="html.parser")
prodName_raw = soup.find_all('h2', {'itemprop':['name']})
prodPrice_raw = soup.find_all('span', {'itemprop':['price']})
driver.quit()
prodName = []
for i in range(len(prodName_raw)):
    prodName.append('')
    prod = str(prodName_raw[i])
    prodName[i] = prod[20:-5]
prodPrice = []
for i in range(len(prodPrice_raw)):
    prodPrice.append('')
    prod = str(prodPrice_raw[i])
    prodPrice[i] = prod[83:-44]
df = pd.DataFrame({'Название': prodName, 'Цена (руб)': prodPrice})
df.to_excel('./iotvega_product_names_and_prices.xlsx', index=False)
print(df)
