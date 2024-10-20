from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

d={'title': [], 'price': []}
driver = webdriver.Chrome()
query="laptop"
for i in range(1,20):
  driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2HSMLFS9POS1P&sprefix=mobile%2Caps%2C285&ref=nb_sb_noss_1")
  #elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")
  elems=driver.find_elements(By.XPATH, "//h2/a/span")
  prices= driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

  print(f"{len(elems)} elements found")
  for elem,price in zip(elems,prices):
    d['price'].append(price.text)
    d['title'].append(elem.text)
  #print(elem.get_attribute("outerHTML"))
driver.close()

df=pd.DataFrame(data=d)
df.to_csv("laptop_data_selenium.csv")