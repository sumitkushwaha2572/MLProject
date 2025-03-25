# A logger is used to track, record, and debug a program's execution. Instead of just printing messages with print(), logging helps store information in a structured way.

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)      # logs is file name 
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# Exception Handling + Logging = Debugging Made Easy!

#Logging stores errors for debugging later.

#Custom Exceptions give clear error messages instead of generic ones.

#No crashes → The system keeps running smoothly.