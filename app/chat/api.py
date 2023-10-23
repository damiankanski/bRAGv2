from fastapi import APIRouter

import openai
from starlette.responses import StreamingResponse

from app.chat.models import BaseMessage, Message
from app.chat.services import OpenAIService
from app.chat.exceptions import OpenAIExceptions


router =APIRouter(tags=["Api Endpoints"])

@router.post("/v1/compltion")
async def complection_create(input_message: BaseMessage) -> Message:
    try:
        return await OpenAIService.chat_completion(input_message=input_message)
    except openai.OpenAIError:
        raise OpenAIExceptions

@router.post("/v1/completion-sream")
async def completion_stream(input_message: BaseMessage) -> StreamingResponse:
    """Streaming response won't return json but rather a properly formatted string for SSE>"""
    try:
        return  await OpenAIService.chat_completion_with_streaming(input_message=input_message)
    except:
        raise OpenAIExceptions



