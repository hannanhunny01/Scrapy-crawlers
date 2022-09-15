from email.policy import default
from itertools import count
from lib2to3.pgen2 import driver
from jmespath import search
import scrapy
from scrapy_selenium import SeleniumRequest
import json
from selenium.webdriver.common.keys import Keys
from sqlalchemy import true
from scrapy.selector import Selector
import numpy as np
from pymongo import MongoClient
from time import sleep
from selenium import webdriver



class SpiderprocuranomeSpider(scrapy.Spider):
    name = 'spiderProcuraNome'







 

   
#print(arrays)

#for name in nomes:
#print(array_nomes)


#    count=0
#    for nome in arrays_of_names:
    
   
#      y =arrays_of_names[count]['nome']
#      count =count+1
#      print(y)
  

   
       
        

    def start_requests(self):
        yield SeleniumRequest(
            url="https://security.cebraspe.org.br/PAS_21/Consulta1Chamada2Semestre_582AECCD/default.aspx",
            wait_time=5,
            screenshot=true,
            callback=self.parse
        )

        
      
    
    def parse(self, response):

       
        
     #  img = response.meta['screenshot']

    #  with open('screenshot.png','wb') as f:
     #   f.write(img)

      #  pessoas_found=[]
        count=0
        cluster = MongoClient("mongodb+srv://cebraspe-tracker:cebraspe-tracker@cluster0.sa63e.mongodb.net/?retryWrites=true&w=majority")

        db = cluster["mainapp"]
        collection_users = db["users"]
        total_users = collection_users.count_documents({})
        array_nomes =  list(collection_users.find({},{'username':1,'_id':0}))
        arrays_of_names = np.array(array_nomes)
        
        for i in range(total_users+1):
            driver= response.meta['driver']
            searchinput = driver.find_element("xpath",'//*[@id="txtNome"]')

            nome = arrays_of_names[count]['username']
            driver.find_element("xpath",'//*[@id="txtNome"]').clear()
      #    searchinput.send_keys('Matheus Rodrigues da Silva')
            searchinput.send_keys(nome)
          
            driver.find_element("xpath",'//*[@id="btnBuscar"]').click()
            
        #searchinput.send_keys(Keys.ENTER)
            driver.save_screenshot(str(count)+'search.png')


            html = driver.page_source
            count=count+1
            sleep(10)
            
            response_obj = Selector(text=html)

            sleep(10)

            #found = response_obj.xpath("//*[@id='GridView1']/tbody/tr[2]/td[2]/text()").get().strip()
          #  pessoas_found.append(found)
        
            yield{
                
                'item':response_obj.xpath("//*[@id='GridView1']/tbody/tr[2]/td[2]/text()").get(default='').strip()
                   
            }
            sleep(10)
           
            
            
            driver.back()
            
            
        driver.quit()  
       

            

       
