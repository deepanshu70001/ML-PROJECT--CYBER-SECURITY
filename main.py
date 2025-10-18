import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    try:
        trainpipelineconfig=TrainingPipelineConfig()
        data_ingestionconfig=DataIngestionConfig(trainpipelineconfig)
        dataingestion=DataIngestion(data_ingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)