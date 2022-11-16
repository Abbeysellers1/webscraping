from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url= 'https://markets.businessinsider.com/cryptocurrencies'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


page = urlopen(url)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

#tbody= soup.find('tbody').findAll('tr')
tbody=soup.find('tbody')
crypto_rows=soup.findAll('tr')

#Find a 'scrappable' cryptocurrencies website where you can scrape 
#               the top 5 cryptocurrencies and display as a formatted output one currency at a time. 
#               The output should display the name of the currency, the symbol (if applicable), 
#               the current price and % change in the last 24 hrs and corresponding price 
#               (based on % change)
# Furthermore, for Bitcoin and Ethereum, the program should alert you via text 
#               if the value falls below $40,000 for BTC and $3,000 for ETH.
# Submit your GitHub URL which should contain all the files worked in class as well as the above.



#NOTES FOR GRADER-THERE WAS NO SYMBOL ON THE WEBSITE!! AND THE PRICE CHANGE WAS ON THERE SO I JUST
#GOT THE CODE TO RUN BY USING SUBTRACTION OF THE TWO. 
for row in crypto_rows[1:6]:
    td = row.findAll('td')
    if td:
        name=(td[0].text)
        numChange= float(td[2].text)
        price=float(td[1].text.replace(',',''))
        percentChange=float(td[3].text.replace('%',''))
        corresponding= (float(price))-(float(numChange))
    
        print(f"Name of Currency: {name}")
        print(f"Current Price: ${price}")
        print(f"Percentage change: {percentChange}%")
        print(f"Corresponding Price: ${corresponding}")
        input()

import keys
from twilio.rest import Client
client=Client(keys.accountSID, keys.myToken)
TwilioNumber = '+16297774452'
myCellphone= '+12817485033'

for row in crypto_rows:
    td = row.findAll('td')
    if td:
        if td[0].text == 'Bitcoin' and float(td[1].text.replace(',',''))<40000:
            textmessage = client.messages.create(to=myCellphone, from_= TwilioNumber, body=(f"The value of Bitcoin (BTC) fell below $40000 and is currently valued at ${float(td[1].text.replace(',',''))}"))
        if  td[0].text == 'Etherium' and float(td[1].text.replace(',',''))<3000:
            textmessage = client.messages.create(to=myCellphone, from_= TwilioNumber, body=(f"The value of Etherium (ETH) fell below $3000 and is currently valued at ${price}"))