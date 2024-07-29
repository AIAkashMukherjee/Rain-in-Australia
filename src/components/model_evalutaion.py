import os
import sys
import numpy as np
import joblib  # Use joblib for loading XGBoost models
from sklearn.metrics import accuracy_score, f1_score, precision_score
from src.logger.logging import logger
from src.exceptions.expection import CustomException

class ModelEvaluation:
    def __init__(self):
        logger.info("Evaluation started")

    def eval_metrics(self, actual, pred):
        acc = accuracy_score(actual, pred)
        f1 = f1_score(actual, pred)
        precision = precision_score(actual, pred)
        logger.info("Evaluation metrics captured")
        return acc, f1, precision

    def initiate_model_evaluation(self, train_array, test_array):
        try:
            X_test, y_test = (test_array[:, :-1], test_array[:, -1])

            model_path = 'model/XGB_model.joblib'
            # Use joblib to load the model
            model = joblib.load(model_path)

            # Make predictions
            prediction = model.predict(X_test)

            acc, f1, precision = self.eval_metrics(y_test, prediction)
            logger.info(f"Evaluation metrics - Accuracy: {acc}, F1 Score: {f1}, Precision: {precision}")

            return acc, f1, precision

        except Exception as e:
            logger.error(f'Error occurred: {e}')
            raise CustomException(e, sys)
