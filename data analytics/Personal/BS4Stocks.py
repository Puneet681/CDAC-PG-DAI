import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.nseindia.com/companies-listing/corporate-filings-financial-results'

response = requests.get(url)
print(response.text)


# html_soup = BeautifulSoup(response.text,'html.parser')
# type(html_soup)
# # print(html_soup)

# movie_containers = html_soup.find_all('div' , class_ = 'lister-item mode-advanced')

# print(type(movie_containers))
# print(len(movie_containers))

# frist_movie = movie_containers[0]
# print(frist_movie)

# # h3 = frist_movie.find("a")
# # h3[1]
# print(frist_movie.h3)
# print(frist_movie.h3.a)
# print(frist_movie.h3.a.text)

# y = frist_movie.find('span' , class_ = 'lister-item-year text-muted unbold')
# print(y)
# print(y.text)


# r = frist_movie.find('div' , class_ = 'inline-block ratings-imdb-rating')
# print(r.strong)
# print(r.strong.text)


# name = []
# rating =  []
# years = []

# for movie in movie_containers:
#     try:
#         name.append(movie.h3.a.text)
#     except:
#         name.append('nan')
#     try:
#         r = movie.find('div' , class_ = 'inline-block ratings-imdb-rating')
#         rating.append(r.strong.text)

#     except:    
#         rating.append('nan')
#     try:
#         y = movie.find('span' , class_ = 'lister-item-year text-muted unbold')
#         years.append(y.text)
#     except:        
#         years.append('nan')

# # print(name,years,rating)

# data = {'name':name , 'year':years,'rating':rating}
# print(data)

# import pandas as pd 

# db = pd.DataFrame(data)
# print(db)
