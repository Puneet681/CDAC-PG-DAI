import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'

response = requests.get(url)
# print(response.text)


html_soup = BeautifulSoup(response.text,'html.parser')
type(html_soup)
html_soup

oscar_title = html_soup.find_all('tr' , style = 'background:#FAEB86')
name = []
year = []
dir = []

for i in range(len(oscar_title)):
    try:
        name.append(oscar_title[i].td.i.b.a.text)
    except:
        name.append('nan')
    try:
        ln = "https://en.wikipedia.org"+oscar_title[i].td.i.b.a['href']
        response = requests.get(ln)
        
        new_html_soup = BeautifulSoup(response.text,'html.parser')
        type(new_html_soup)
        new_html_soup
        oscar_year = new_html_soup.find_all('span' , class_ = 'bday dtstart published updated')
        year.append(oscar_year[0].text)
    except:
        year.append('nan')
    try:
        director = new_html_soup.find('td',class_ = 'infobox-data').text
        dir.append(director)
    except:
        dir.append('Nan')
        
df = pd.DataFrame({'Movie Name':name,'director':dir,'year':year})

print(df)