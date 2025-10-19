import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    try:
        trainpipelineconfig=TrainingPipelineConfig()
        data_ingestionconfig=DataIngestionConfig(trainpipelineconfig)
        dataingestion=DataIngestion(data_ingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("data ingestion completed")
        data_validation_config=DataValidationConfig(training_pipeline_config=trainpipelineconfig)
        data_valid=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        logging.info("initialte data validation")
        data_validation_artifact=data_valid.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
    except Exception as e:
        raise CustomException(e,sys)