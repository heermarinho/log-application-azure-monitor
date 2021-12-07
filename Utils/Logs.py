import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from uuid import uuid4 
from datetime import datetime as dt 
from time import sleep
logger = logging.getLogger(__name__)

# TODO: replace the all-zero GUID with your instrumentation key.
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=FREE KEY')
)

def log_app(msg):
    #line = input("Enter a value: ")
    msg = str(uuid4())+" | "+msg
    print(msg)
    logger.warning(msg)
    sleep(1)
