from src.logger.logging import logger
from src.exceptions.expection import CustomException
from sklearn.preprocessing import StandardScaler,OrdinalEncoder,LabelEncoder
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.utlis.utlis import save_obj
import numpy as np
import pandas as pd
import os
import sys


@dataclass
class DataTransformationConfig:
    preprocessor_obj=os.path.join('artifact/data_transformation', 'preprocessor.pkl')

class DataTransfomation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logger.info('Data Transformation started')
            cat_columns=[
                'RainToday','Location','WindGustDir','WindDir9am',
                'WindDir3pm'
            ]

            num_columns=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation','Sunshine',
            'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
            'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
            'Temp9am', 'Temp3pm']
    
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OrdinalEncoder())
                
                ]

            )
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,num_columns),
                    ('categorical_pipeline',cat_pipeline,cat_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            logger.info('Problem in get data transformation')
            raise CustomException(e,sys)      

    def initate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logger.info("Read train and test data completed")

            preprocessing_obj=self.get_data_transformation()

            target_column_name='RainTomorrow'
            drop_columns=['Date',target_column_name]

            train_df = train_df.dropna(subset=[target_column_name])
            test_df = test_df.dropna(subset=[target_column_name])

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]

            label_encoder = LabelEncoder()
            target_feature_train_encoded = label_encoder.fit_transform(target_feature_train_df)
            target_feature_test_encoded = label_encoder.transform(target_feature_test_df)


            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
            input_feature_train_arr, np.array(target_feature_train_encoded)
            ]
            test_arr = np.c_[
            input_feature_test_arr, np.array(target_feature_test_encoded)
            ]

            save_obj(
            file_path=self.data_transformation_config.preprocessor_obj,
            obj=preprocessing_obj
        )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj
            )
        except Exception as e:
            logger.info('Problem in data transformation')
            raise CustomException(e,sys)