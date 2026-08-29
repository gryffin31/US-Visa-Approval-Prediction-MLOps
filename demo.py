from us_visa.logger import logging
from us_visa.exception import USvisaException

import sys

logging.info("Welome to our custom log")

try:
    a = 2/0
except Exception as e:
    logging.info("We are dividing by zero")
    raise USvisaException(e, sys)

