import os
import sys
import json
import pymongo
import certifi
from dotenv import load_dotenv
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
import pandas as pd
import numpy as np
from networksecurity.logging.logger import logging

load_dotenv()
mongo_DB_URL=os.getenv("MONGO_DB_URL")
print(mongo_DB_URL)

import certifi
ca=certifi.where()

class network_data_extract():


    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(mongo_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return (len(self.records))
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    file_path="Network_Data\phisingData.csv"
    database="ml_prpject"
    collection="NetworkData"
    obj=network_data_extract()
    records=obj.csv_to_json(file_path=file_path)
    no_of_record=obj.insert_data_mongo(records=records,database=database,collection=collection)
    print(no_of_record)