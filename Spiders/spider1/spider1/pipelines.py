import collections
from itemadapter import ItemAdapter
import logging
import pymongo
from time import sleep


class CebraspecrawlerPipeline:
    collection_name = "links_de_Href"

    cluster =pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
    db_counts = cluster["counts"]
    collection_count = db_counts["counts_de_links"]

# collection para links (database)
    db2= cluster["hrefs"]
    collection2= db2["links_de_Href"]

    
#count = collection2.find().count()

    total_count = collection2.count_documents({})
    print(total_count)
  #  sleep(5)
    collection_count.update_one({"_id":0},{"$set":{"Count-de-href-ultimo":total_count}})

    #apagando collection atual
    collection2.delete_many({})
    
    @classmethod
    
        
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
        self.db =self.client["hrefs"]
        

    
    def close_spider(self,spider):
        self.client.close()
        


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item