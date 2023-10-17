import logging

# prepare logging settings

logging.basicConfig(level=logging.INFO)

# create logger which ensure common configuration for the future with our format
logger = logging.getLogger(__name__)

# push logs to console
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)
