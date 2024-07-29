import os,sys
from src.components.data_transformation import DataTransfomation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path , test_data_path = obj.initate_data_ingestion()     

    data_transformation = DataTransfomation()
    train_arr, test_arr, _ = data_transformation.initate_data_transformation(train_data_path , test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_trainer(train_arr,test_arr)

   