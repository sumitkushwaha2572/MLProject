import sys
from src.loggers import logging

#def error_message_detail(error,error_detail:sys):
 #   _,_,exc_tb=error_detail.exc_info()                            # on which line error and which file is occured all detail comes here 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):               ## we created class inherited the exception
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


  #  What happens here?

# This function takes two parameters:

# error: The actual exception/error object.

# error_detail: The sys module, which helps extract system-related details like tracebacks.

#  Why use sys?

# The sys module allows us to retrieve detailed error information using sys.exc_info().


# sys.exc_info() returns three values:

# Exception type (e.g., ZeroDivisionError)

#Exception value (the actual error message, e.g., "division by zero")

#Traceback object (exc_tb) → Contains information about where the error occurred.