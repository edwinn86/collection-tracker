#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
import csv
  
URL = "https://www.pricecharting.com/game/pokemon-evolving-skies/booster-box" 
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
# print(soup.prettify()) 

price = []

table = soup.find('span', attrs = {'class':'price js-price'})
for row in table:
    price.append(row)

print(price[0].strip())

"""
with open('data.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for row in soup:
        writer.writerow(row) """