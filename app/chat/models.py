from pydantic import BaseModel, Field

from constants import ChatRolesEnum, ModelsEnum
from app.core.models import TimestampAbstractModel

class BaseMessage(BaseModel):
    """Basee pydentic model that we use to interat with the Api"""
    model: ModelsEnum = Field(default=ModelsEnum.GPT4.value)
    message: str

class Message(TimestampAbstractModel, BaseMessage):
    role: ChatRolesEnum

