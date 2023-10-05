import scrapy
import time
import requests
import pandas as pd
class AwardSpider(scrapy.Spider):
    name = 'IMDb_spider'
    start_urls = ['https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-01']

    def parse(self,response):
        data = {}
        # #data['title'] = response.css("title::text").extract()
        # #used to create generator/iterable function like range 
        movie_blocks = response.css("div[class='lister-item-content']")
        for movie in movie_blocks:
            data['title'] = movie.css(r"h3[class='lister-item-header'] a[href]::text").get()
            data['rating'] = movie.css(r"div[class = 'inline-block ratings-imdb-rating'] strong::text").get()
            data['year'] = movie.css(r"span[class = 'lister-item-year text-muted unbold']::text").get()
            data['certificate'] = movie.css(r"span[class = 'certificate']::text").get()
            data['voted'] = movie.css(r"span[name = 'nv']::text").get()
            a = movie.css(r"span[class = 'genre']::text").get()
            data['genre'] = (str(a).lstrip('\n')).rstrip(' ')
            yield data
        
        print(data)