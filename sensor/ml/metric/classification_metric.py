from sensor.entity.artifact_entity import ClassificationMetricArtifact
from sensor.exception import SensorException
from sklearn.metrics import f1_score,precision_score,recall_score
from sensor.logger import logging
import os,sys
import pandas as pd

def get_classifiaction_score(y_true,y_pred)-> ClassificationMetricArtifact:
    try:
        logging.info(f"y_true values:{y_true}")
        logging.info(f"y_pred values:{y_pred}")
        model_f1_score = f1_score(y_true,y_pred)
        model_recall_score = recall_score(y_true,y_pred)
        model_precision_score = precision_score(y_true,y_pred)

        Classification_metric =  ClassificationMetricArtifact(f1_score=model_f1_score,
                                            preision_score=model_precision_score,
                                            recall_score=model_recall_score)
        return Classification_metric
    except Exception as e:
        raise SensorException(e,sys)