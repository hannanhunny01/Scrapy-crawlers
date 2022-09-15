# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import collections

import logging
import pymongo



class Spider3Pipeline:
    collection_name = "names_found"
    cluster =pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")

    db_user_found= cluster["mainapp"]
    collection2= db_user_found["names_found"]
    collection2.delete_many({})


    def open_spider(self,spider):

        self.client = pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
        self.db =self.client["mainapp"]
    
    def close_spider(self,spider):
        self.client.close()
        
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)

        return item
