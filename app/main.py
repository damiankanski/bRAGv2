from fastapi import FastAPI

from app import version
from app.core.logs import logger

app = FastAPI(version=version)
logger.info("App is ready!")