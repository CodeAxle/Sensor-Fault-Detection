from sensor.configuration.mongo_db_connection import MongoDBclient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
from sensor.pipeline import training_pipeline
from sensor.logger import logging
import os,sys
if __name__ =='__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipline()

    except Exception as e:
        raise SensorException(e,sys)