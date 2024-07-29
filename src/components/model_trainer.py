import os
import sys
from src.logger.logging import logger
from src.exceptions.expection import CustomException
from dataclasses import dataclass
from src.utlis.utlis import save_obj, evaluate_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import pandas as pd
import numpy as np

@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join('artifact/model_trainer', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initate_model_trainer(self, train_array, test_array):
        try:
            # Extract features and target
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            
            # Define models and parameters
            models = {
                "Random Forest": RandomForestClassifier(),
                "XGboost": XGBClassifier(),
                "Logistic": LogisticRegression()
            }

            params = {
                "Random Forest": {
  
                    "n_estimators": [90, 120, 150, 200],
                    "max_depth": [10, 8, 5],
                    "min_samples_split": [2, 5, 10],
                },
                "XGboost": {
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 5, 7],
                    "min_child_weight": [1, 3, 5],
                    "gamma": [0, 0.1, 0.3],
                    "subsample": [0.6, 0.8, 1.0],
                    "colsample_bytree": [0.6, 0.8, 1.0],
                    "n_estimators": [100, 200, 300]
                },
                "Logistic": {

                    "penalty": ['l1', 'l2'],
                    "C": [0.001, 0.01, 0.1, 1, 10, 100],
                    "solver": ['liblinear', 'saga']
                }
            }

            # Evaluate models
            model_report = evaluate_model(models, X_train, X_test, y_train, y_test, params)
            print(model_report)
            print('\n====================================================================================\n')
            logger.info(f'Model Report: {model_report}')

            # Get the best model score
            best_model_score = max(model_report.values())
            best_model_name = [name for name, score in model_report.items() if score == best_model_score][0]
            best_model = models[best_model_name]

            print(f"Best Model Found, Model Name is: {best_model_name}, Accuracy_Score: {best_model_score}")
            print("\n***************************************************************************************\n")
            logger.info(f"Best model found, Model Name is {best_model_name}, Accuracy Score: {best_model_score}")

            # Save the best model
            save_obj(file_path=self.model_trainer_config.train_model_file_path, obj=best_model)

        except Exception as e:
            logger.error(f'Error occurred: {e}')
            raise CustomException(e, sys)
