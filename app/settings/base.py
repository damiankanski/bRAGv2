from pydantic import Field
from pydantic_settings import BaseSettings

from app.core.constants import Environments


class Settings(BaseSettings):
    APP_NAME: str = "bRAGv2"
    ENVIRONMENT: str = Field(env="ENVIRONMENT", default=Environments.LOCAL.value)

    DATABASE_URL: str = Field(env="DATABASE_URL")
    OPENAI_API_KEY: str = Field(env="OPENAI_API_KEY")
    GENERATION_TIMEOUT_SEC: int = Field(env="GENERATION_TIMEOUT_SEC", default=120)

    QDRANT_HOST: str = Field(env="QDRANT_HOST", default="localhost")
    QDRANT_API_KEY: str = Field(env="OPENAI_API_KEY", default="None")
    QDRANT_COLLECTION_NAME: str = Field(env="QDRANT_COLLECTION_NAME", default="demo")
    @property
    def is_local(self):
        return self.ENVIRONMENT == Environments.LOCAL.value

    class Config:
        env_file = ".env"