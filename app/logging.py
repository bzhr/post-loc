import logging

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)
# This logger logs to file
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
# This logger logs to std out
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
