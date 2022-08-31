import collections
from itemadapter import ItemAdapter
import logging
import pymongo



class CebraspecrawlerPipeline:
    collection_name = "links_de_Href"
    
    @classmethod
    
        
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
        self.db =self.client["hrefs"]
        

    
    def close_spider(self,spider):
        self.client.close()
        


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item