from datetime import datetime

from pydantic import BaseModel, Field

#createt realt time model
class TimestampAbstractModel(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)