import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from csv import writer
#Product link
link="https://www.flipkart.com/redmi-10-pacific-blue-64-gb/product-reviews/itm0f2a6a2112b75?pid=MOBGC9GYCHQZK9GW&lid=LSTMOBGC9GYCHQZK9GW8N0WII&marketplace=FLIPKART"
page=requests.get(link)
soup=bs(page.content,'html.parser')
lists=soup.find_all('div',class_="col _2wzgFH K0kLPL")
products=[]
for list in lists:
      review=soup.find('div',class_="")
      products.extend(review.text)
      #Test to show that the code works
      print(review.text)
#To write the results in csv file
df = pd.DataFrame({'Review':products}) 
df.to_csv('product.csv', index=False, encoding='utf-8')