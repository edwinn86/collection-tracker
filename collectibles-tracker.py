#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
import csv

URLS = ["https://www.pricecharting.com/game/pokemon-evolving-skies/booster-box", "https://www.pricecharting.com/game/pokemon-chilling-reign/booster-box?q=chilling+reign+booster+box", 
        "https://www.pricecharting.com/game/pokemon-crown-zenith/absol-gg16"]
prices = []

for url in URLS: 
    r = requests.get(url) 
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    # print(soup.prettify()) 


    table = soup.find('span', attrs = {'class':'price js-price'})
    for row in table:
        prices.append(float(row.strip()[1:]))

print(prices)

with open('data.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for p in prices:
        writer.writerow([p]) 