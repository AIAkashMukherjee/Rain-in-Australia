# Create prediction pipeline class -> completed
# create function for load a object -> completed
# Create custome class basd upon our dataset -> completed
# Create function to convert data into Dataframe with the help of Dict

import os,sys
from src.logger.logging import logger
from src.exceptions.expection import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion
from src.utlis.utlis import load_obj
import pandas as pd


class PredicitonPipeline:
    def __init__(self) -> None:
        pass

    def predict(self,features):
        preprocessor_obj_path=os.path.join("artifact/data_transformation", "preprocessor.pkl")

        model_path=os.path.join("artifact/model_trainer", "model.pkl")
        
        processor=load_obj(preprocessor_obj_path)
        model=load_obj(model_path)

        scaled=processor.transform(features)
        pred=model.predict(scaled)

        return pred
    

class CustomClass:
    def __init__(self,
                 Location:int,
                  MinTemp:int, 
                  MaxTemp:int, 
                  Rainfall:int, 
                  Evaporation:int,
                  Sunshine:int,  
                  WindGustDir:int,
                  WindGustSpeed:int,  
                  WindDir9am:int, 
                  WindDir3pm:int,
                  WindSpeed9am:int, 
                  WindSpeed3pm:int,
                   Humidity9am :int,
                  Humidity3pm:int,  
                  Pressure9am:int, 
                  Pressure3pm:int,
                  Cloud9am:int,
                   Cloud3pm :int,
                  Temp9am:int,  
                  Temp3pm:int, 
                  RainToday:int
                 
                  ):
    
        # Initialize all attributes
        self.Location = Location
        self.MinTemp = MinTemp
        self.MaxTemp = MaxTemp
        self.Rainfall = Rainfall
        self.Evaporation = Evaporation
        self.Sunshine = Sunshine
        self.WindGustDir = WindGustDir
        self.WindGustSpeed = WindGustSpeed
        self.WindDir9am = WindDir9am
        self.WindDir3pm = WindDir3pm
        self.WindSpeed9am = WindSpeed9am
        self.WindSpeed3pm = WindSpeed3pm
        self.Humidity9am = Humidity9am
        self.Humidity3pm = Humidity3pm
        self.Pressure9am = Pressure9am
        self.Pressure3pm = Pressure3pm
        self.Cloud9am = Cloud9am
        self.Cloud3pm = Cloud3pm
        self.Temp9am = Temp9am
        self.Temp3pm = Temp3pm
        self.RainToday = RainToday

    def get_data_DataFrame(self):
        try:
            custom_input = {
                "Location": [self.Location],
                "MinTemp": [self.MinTemp],
                "MaxTemp": [self.MaxTemp],
                "Rainfall": [self.Rainfall],
                "Evaporation": [self.Evaporation],
                "Sunshine": [self.Sunshine],
                "WindGustDir": [self.WindGustDir],
                "WindGustSpeed": [self.WindGustSpeed],
                "WindDir9am": [self.WindDir9am],
                "WindDir3pm": [self.WindDir3pm],
                "WindSpeed9am": [self.WindSpeed9am],
                "WindSpeed3pm": [self.WindSpeed3pm],
                "Humidity9am": [self.Humidity9am],
                "Humidity3pm": [self.Humidity3pm],
                "Pressure9am": [self.Pressure9am],
                "Pressure3pm": [self.Pressure3pm],
                "Cloud9am": [self.Cloud9am],
                "Cloud3pm": [self.Cloud3pm],
                "Temp9am": [self.Temp9am],
                "Temp3pm": [self.Temp3pm],
                "RainToday": [self.RainToday]
            }
            data=pd.DataFrame(custom_input)
            return data
        except Exception as e:
            raise CustomException(e,sys)    


