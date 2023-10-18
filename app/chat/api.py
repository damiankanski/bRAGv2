from fastapi import APIRouter

import openai

from app.chat.models import BaseMessage, Message
from app.chat.services import OpenAIService
from app.chat.exceptions import OpenAIExceptions


router =APIRouter(tags=["Core Endpoints"])

@router.post("/v1/compltion")
async def complection_create(input_message: BaseMessage) -> Message:
    try:
        return await OpenAIService.chat_completion(input_message=input_message)
    except openai.OpenAIError:
        raise OpenAIExceptions

