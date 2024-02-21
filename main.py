from sensor.config.mongo_db_connection import MongoDBclient


if __name__ =='__main__':
    mongob_client = MongoDBclient()
    print("Collection_name:",mongob_client.database.list_collection_names())