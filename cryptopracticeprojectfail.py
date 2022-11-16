from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url= 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


page = urlopen(url)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title
print(url)
print(title)

#tbody= soup.find('tbody').findAll('tr')
tbody=soup.find('tbody')
tables = tbody[0]

print(tables)
crypto_rows=tables.findAll('tr')

print()
print(crypto_rows)
p = crypto_rows.findAll("p")
#  , attrs={'class':'p'})
# caret= crypto_rows.findAll("span",attrs={'class':"icon-Caret-up"})

#Find a 'scrappable' cryptocurrencies website where you can scrape 
#               the top 5 cryptocurrencies and display as a formatted output one currency at a time. 
#               The output should display the name of the currency, the symbol (if applicable), 
#               the current price and % change in the last 24 hrs and corresponding price 
#               (based on % change)
# Furthermore, for Bitcoin and Ethereum, the program should alert you via text 
#               if the value falls below $40,000 for BTC and $3,000 for ETH.
# Submit your GitHub URL which should contain all the files worked in class as well as the above.

#make an upper and lower arrow if statement and function  

for row in crypto_rows[1:6]:
    td = row.findAll('td')
    if td:
        name=(p[1].text)
        symbol= (p[2].text)
        
        price=float(td[3].text.replace(',','').replace('$',''))
        #change=float(((td[4].text).replace('%',''))*.01)
        '''if caret[0]== 'icon-Caret-up':
            change==change
        else: 
            change==('-'+change)'''
        #corresponding= float(price/(change+1))
        print(f"Name of Currency: {name}")
        print(f"Symbol: {symbol}")
        print(f"Current Price: ${price}")
        #print(f"Percentage change: {change}%")
        #print(f"Corresponding Price: ${corresponding}")
        input()

import keys

from twilio.rest import Client
client=Client(keys.accountSID, keys.myToken)
TwilioNumber = '+16297774452'
myCellphone= '+12817485033'
price= float(price)

if name == 'Bitcoin' and price<40000:
    textmessage = client.messages.create(to=myCellphone, from_= TwilioNumber, body=(f"The value of Bitcoin (BTC) fell below $40000 and is currently valued at ${price}"))

if name == 'Etherium' and price<3000:
    textmessage = client.messages.create(to=myCellphone, from_= TwilioNumber, body=(f"The value of Etherium (ETH) fell below $3000 and is currently valued at ${price}"))