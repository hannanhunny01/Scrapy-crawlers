import collections
from itemadapter import ItemAdapter
import logging
import pymongo



class CebraspecrawlerPipeline:
    collection_name = "links_de_Chamada"
    cluster =pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
    db_count = cluster["counts"]
    collection_count = db_count["counts_de_links"]

# collection para links (database)
    db2= cluster["links"]
    collection2= db2["links_de_Chamada"]


#count = collection2.find().count()

    total_count = collection2.count_documents({})
    #print(total_count)
    collection_count.update_one({"_id":0},{"$set":{"Count-de-Chamadas-ultimo":total_count}})

    #apagando collection atual
    collection2.delete_many({})

    
    @classmethod
    
        
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")
        self.db =self.client["links"]
        

    
    def close_spider(self,spider):
        self.client.close()
        


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)

        return item