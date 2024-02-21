import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi


ca= certifi.where()

class MongoDBclient:
    client = None

    
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBclient.client is None:
                mongo_db_url="mongodb+srv://Avishil_07:Prinxe_1724@cluster0.xjqpcwb.mongodb.net/?retryWrites=true&w=majority"
                MongoDBclient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client = MongoDBclient.client
            self.database =self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            raise e