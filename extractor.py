import json
import pymongo

class NewsExtractor():
    collection = "articles_collection"
    # search_query = ""
    def __init__(self):
        self.conn=pymongo.MongoClient('localhost',27017)
        db=self.conn['mynews']
        self.collection=db['news_table']


    def search(self, query):
        result = []    
        newsList = self.collection.find()
        for item in newsList:
            if query in item["headline"] or query in item["text"]:
                result.append(item)
        # result = self.collection.find({"text":query})
     
        return result
    
    

search_query = input()
extractor = NewsExtractor()
docs = extractor.search(search_query)
for x in docs:
    print(x)