import scrapy
from movies.items import MoviesItem
import lxml.etree
from scrapy.selector import Selector

class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com/films?showType=3']
    start_urls = ['http://maoyan.com/films?showType=3/']

    # def start_requests(self):
    #     for i in range(0, 10):
    #         url = 'http://maoyan.com/films?showType=3/'
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        item = MoviesItem()
        name_movies=[]
        type_movies=[]
        time_movies=[]
        movies=Selector(response=response).xpath('//div[@class="movie-item-hover"]')
       #//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()
        count=0
        for movie in movies:
            if count==10:
                break
            name_movie=movie.xpath('./a/div/div[1]/span[1]/text()').extract()
            type_movie=movie.xpath('./a/div/div[2]/text()').extract()
            time_movie = movie.xpath('./a/div/div[4]/text()').extract()
            name_movies.append(name_movie[0])
            type_movies.append(type_movie[1].strip())
            time_movies.append(time_movie[1].strip())
            # print(type_movie.split('\n')[2].strip())
            # print(time_movie.split('\n')[2].strip())
            count=count+1
        print(name_movies)
        print(type_movies)
        print(time_movies)
        item["name_movies"]= name_movies
        item["type_movies"] = type_movies
        item["time_movies"] = time_movies
        return item


        # pass

