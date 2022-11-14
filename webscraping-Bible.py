import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


url='https://ebible.org/asv/JHN01.htm'

#https://ebible.org/asv/JHN05.htm


random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = '0'+ str(random_chapter)
else:
    random_chapter =str(random_chapter)


webpage = 'https://ebible.org/asv/JHN'+ random_chapter + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage =urlopen(req).read()
soup=BeautifulSoup(webpage, 'html.parser')     #these two lines will always be included

#label= soup.findAll('div', attrs= {'class': 'chapterlabel'})
#print(label)
#random_verse= random.randint()

page_verses = soup.findAll("div", attrs={'class':'main'})

verse_list=[]

for verse in page_verses:
    #print(verse)
    verse_list = verse.text.split(".")

myverse = 'Chapter: ' + random_chapter + ' Verse: ' + random.choice(verse_list[:len(verse_list)-2])
print(myverse)

import keys

from twilio.rest import Client
client=Client(keys.accountSID, keys.myToken)

TwilioNumber = '+16297774452'
myCellphone= '+12817485033'

#send text message
textmessage = client.messages.create(to=myCellphone, from_= TwilioNumber, body=myverse)
'''
one way we could do it would be 
page_verses=soup.findAll('div', attrs={'class': 'main'})

and use a counter and convert to string and back'''




