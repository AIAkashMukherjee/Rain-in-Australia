import os
import logging
from pathlib import Path

list_of_files=[
    '.github/.workflows/.gitkeep', # for pushing file to github
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evalutaion.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utlis/__init__.py',
    'src/utlis/utlis.py',
    'src/logger/logging.py',
    'src/logger/__init__.py',
    'src/exceptions/expection.py',
    'src/exceptions/__init__.py',
    # 'tests/unit/__init__.py',
    # 'tests/integration/__init__.py',
    'init_setup.sh',
    'setup.py',
    'setup.config' 
]


for filepath in list_of_files:
    file=Path(filepath)
    file_dir,file_name =os.path.split(file)
    if file_dir!='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'Creating Directory {file_dir} for file {file_name}')

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,'w')as f:
            pass    # this will create empty file   
