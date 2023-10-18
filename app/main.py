from fastapi import FastAPI

from app import version
from app.core.api import router as core_router
from app.core.logs import logger

app = FastAPI(version=version)
app.include_router(core_router)

logger.info("App is ready!")
