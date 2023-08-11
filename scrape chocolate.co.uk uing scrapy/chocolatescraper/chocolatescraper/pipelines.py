# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import mysql.connector

class ChocolatescraperPipeline:
    def process_item(self, item, spider):
        return item


class PriceToUSDPipeline:
    gbpTOUSDRate = 1.3

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('price'):
            floatPrice = float(adapter['price'])
            adapter['price']= floatPrice * self.gbpTOUSDRate

            return item
        
        else: 
            raise DropItem(f'Missing price in {item}')
        


class DuplicatesPipeline:

    def __init__(self):
        self.name_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter['name'] in self.name_seen:
            raise DropItem(f'Duplicate item found {item!r}')
        
        else:
            self.name_seen.add(adapter['name'])
            return item
        

# class SavingToMySQLPipline(object):
#     def __init__(self):
#         self.create_connection()

#     def create_connection(self):
#         self.connection = mysql.connector.connect(
#             host = 'localhost',
#             user = 'YOUR_USERNAME',
#             pasword = 'YOUR_PASSWORD',
#             database = 'chocolate_scraping',
#             port = '3306'
#             )
            
#         self.curr = self.connection.cursor()

#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item

#     def store_db(self, item):
#         self.curr.execute('''insert into chocolate_products (name, price, url) value (%s, %s, %s)''',(
#                           item['name'],
#                           item['price'],
#                           item['url']
#                           ))
#         self.connection.commit()
        
#         self.curr.close()
#         self.connection.close()
        
import pymysql.cursors

class SavingToMySQLPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='YOUR_USERNAME',
            password='YOUR_PASSWORD',
            database='chocolate_scraping',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )
            
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute('''INSERT INTO chocolate_products (name, price, url) VALUES (%s, %s, %s)''', (
            item['name'],
            item['price'],
            item['url']
        ))
        self.connection.commit()
        
    def close_spider(self, spider):
        self.curr.close()
        self.connection.close()
