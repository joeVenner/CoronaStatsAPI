import urllib.request
import requests
from time import sleep
from bs4 import BeautifulSoup



alldata = {}

def data():

    while True:
        url = 'https://www.worldometers.info/coronavirus/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table', attrs={'id': 'main_table_countries_today'})
        last_update = soup.find('div', attrs={'class': 'label-counter'})
        div_next = last_update.find_next('div')

        table_body = table.find('tbody')
        rows = table_body.findChildren('tr')

        for row in rows:
            countrydata = []
            cells = row.findChildren('td')
            for cell in cells:
                countrydata.append(cell.string)

            if countrydata[0] != None:
                alldata[countrydata[1]] = countrydata

        alldata["lastupdate"]=div_next.text
      
        sleep(1800)
