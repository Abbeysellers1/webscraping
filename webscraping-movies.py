from urllib.request import urlopen
from bs4 import BeautifulSoup


#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

movie_rows= soup.findAll('tr')


print(title.text)

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank=(td[0].text)
    release=(td[1].text)
    gross=int(td[7].text.replace(',','').replace('$',''))
    theater=int((td[6].text).replace(',',''))
    gross_theater= round((gross/theater),2)
    distributor= (td[9].text)

    print(f"Rank: {rank}")
    print(f"Release: {release}")
    print(f"Total Gross: ${gross}")
    print(f"Distributor: {distributor}")
    print(f"Average Gross per Theater: ${gross_theater}")
    input()

##
##
##
##

