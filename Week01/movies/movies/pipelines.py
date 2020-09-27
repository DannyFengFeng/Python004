# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviesPipeline:
    def process_item(self, item, spider):
        name_movies = item['name_movies']
        type_movies = item['type_movies']
        time_movies = item['time_movies']
        print("111111111111111111111111111111111111111111111111111111111111111111")
        output = ''.join(name_movies)+''.join(type_movies)+''.join(time_movies)
        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
