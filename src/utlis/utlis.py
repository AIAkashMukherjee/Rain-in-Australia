from src.exceptions.expection import CustomException
from src.logger.logging import logger
import sys,os
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV

def save_obj(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,'wb')as f:
            pickle.dump(obj,f)

    except Exception as e:
        logger.info(f'Error ocuured in {e}')
        raise CustomException(e,sys)
    
def load_obj(file_path):
    try:
        with open(file_path,'rb')as f:
            return pickle.load(f)
    except Exception as e:
        logger.info(f'Error ocuured in {e}')
        raise CustomException(e,sys)
    

def evaluate_model(models, X_train, X_test, y_train, y_test, params):
    try:
        report = {}
        for model_name, model in models.items():
            param = params.get(model_name, {})

            # Initialize RandomizedSearchCV
            rs = RandomizedSearchCV(model, param, cv=7, random_state=42, n_jobs=-1, n_iter=100)
            rs.fit(X_train, y_train)

            logger.info('Fitting the model')
            # Set the best parameters and refit the model
            model.set_params(**rs.best_params_)
            model.fit(X_train, y_train)

            # Predict and evaluate the model
            y_pred = model.predict(X_test)
            test_model_score = accuracy_score(y_test, y_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        logger.error(f'Error occurred: {e}')
        raise CustomException(e, sys)  
    

