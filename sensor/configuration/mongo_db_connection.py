import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_var import MONGODB_URL_KEY
import certifi
import os

ca= certifi.where()

class MongoDBclient:
    client = None

    
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBclient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                MongoDBclient.client = pymongo.MongoClient(mongo_db_url)
            self.client = MongoDBclient.client
            self.database =self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            raise e
        
