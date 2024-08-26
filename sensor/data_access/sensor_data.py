import sys
from typing import Optional
import numpy as np
import pandas as pd
from sensor.configuration.mongo_db_connection import MongoDBclient
from sensor.exception import SensorException
from sensor.constant.database import DATABASE_NAME
from myenv.Lib import json

class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBclient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException (e,sys)
        
    def save_csv_file(self,file_path ,collection_name: str, database_name: Optional[str] = None):
        try:
            data_frame=pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)
        
    def export_collection_as_dataframe(
            self,collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        try:
            """
            export entire collection as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]

            else:
                collection = self.mongo_client[database_name][collection_name]
        
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=[ "_id"], axis=1)

            df.infer_objects(copy=False)
            pd.set_option('future.no_silent_downcasting', True)
            df.replace({"na":np.nan},inplace=True)

            return df

        except Exception as e:
            raise SensorException (e,sys)
        
"""FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version.
To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. 
To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
df.replace({"na":np.nan},inplace=True)"""