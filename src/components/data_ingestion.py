from src.logger.logging import logger
from src.exceptions.expection import CustomException
from dataclasses import dataclass
import  numpy as np
import pandas as pd
import os,sys
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransfomation


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

@dataclass
class DataIngestionConfig:
    train_file_path=os.path.join('artifact/data_ingestion','train.csv')
    test_file_path=os.path.join('artifact/data_ingestion','test.csv')
    raw_file_path=os.path.join('artifact/data_ingestion','raw.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

    def initate_data_ingestion(self):
        logger.info('Data Ingestion Started')
        try:
            df=pd.read_csv('data/weatherAUS.csv')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_file_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_file_path,index=False)

            train_set,test_set=train_test_split(df,test_size=.2,random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_file_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.test_file_path,index=False,header=True)

            return (
                self.data_ingestion_config.train_file_path,
                self.data_ingestion_config.test_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)  

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path , test_data_path = obj.initate_data_ingestion()     

    data_transformation=DataTransfomation()
    train_arr,test_arr,_=data_transformation.initate_data_transformation(train_data_path,test_data_path)            