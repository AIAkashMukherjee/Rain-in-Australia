import os,sys
from src.logger.logging import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

def error_message_detail(error,error_detail:sys):
    _,_,ex_tb=error_detail.exc_info()

    file_name=ex_tb.tb_frame.f_code.co_filename

    error_msg="Error occured in python script name [{0}] line number [{1}] erro message [{2}]".format(
        file_name, ex_tb.tb_lineno, str(error)
    )

    return error_msg


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys) :
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message    
    

if __name__ =="__main__":
    try:
        a = 1 / 0

    except Exception as e:
        logger.info("Divison by Zero")
        raise CustomException(e,sys)
            