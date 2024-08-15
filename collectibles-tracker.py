#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
import csv

URLS = ["https://www.pricecharting.com/game/pokemon-evolving-skies/booster-box", "https://www.pricecharting.com/game/pokemon-chilling-reign/booster-box?q=chilling+reign+booster+box", 
        "https://www.pricecharting.com/game/pokemon-crown-zenith/absol-gg16"]

names = []
URL = []
amount = []

with open('collection.csv', mode ='r',)as file:
  csvFile = csv.reader(file)
  next(csvFile)
  for line in csvFile:
        print(line)
        names.append(line[0])
        URL.append(line[1])
        amount.append(line[2])
        print(URL, amount)


prices = []

for url in URL: 
    r = requests.get(url) 
    
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    # print(soup.prettify()) 


    table = soup.find('span', attrs = {'class':'price js-price'})
    for row in table:
        prices.append(float(row.strip()[1:]))
    

for i in range(len(amount)):
    prices[i] *= int(amount[i])

print(prices)

with open('values.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for row in zip(names, prices):

        writer.writerow(row) 