import sys
import logging

def error_message_detail(error, err_detail: sys):
    _, _, exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message  # ✅ ADD THIS LINE

class CustomException(Exception):
    def __init__(self, error_message, err_detail: sys):
        super().__init__(error_message)
        self.err_message = error_message_detail(error_message, err_detail)

    def __str__(self):
        return self.err_message

