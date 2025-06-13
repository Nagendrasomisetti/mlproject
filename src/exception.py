import sys
import logging

def error_message_detail(error, detail: sys):
    """
    Extracts the error message and details from an exception.
    """
    _, _, exc_tb = detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line {line_number}: {str(error)}"
    return error_message    

class CustomException(Exception):
    def __init__(self, error, detail: sys):
        self.error_message = error_message_detail(error, detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Division by zero.")
        raise CustomException(e, sys)