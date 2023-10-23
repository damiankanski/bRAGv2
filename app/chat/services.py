import openai
from openai import ChatCompletion
from starlette.responses import StreamingResponse

from app.chat.constants import ChatRolesEnum
from app.chat.models import BaseMessage, Message
from app.core.logs import logger
from settings import settings
from app.db import messages_queries
from streaming import stream_generator

class OpenAIService:
    @classmethod
    async def chat_completion_without_streaming(cls, input_message: BaseMessage) -> Message:
        completion: openai.ChatCompletion = await openai.ChatCompletion.acreate(
            model=input_message.model,
            api_key=settings.OPENAI_API_KEY,
            messages=[{"role": ChatRolesEnum.USER.value, "content": input_message.message}],
        )
        logger.info(f"Got the following response: {completion}")
        message = Message(
            model=input_message.model,
            message=cls.extract_response_from_completion(completion),
            role=ChatRolesEnum.ASSISTANT.value,
        )
        messages_queries.insert(model=message.model, message=message.message, role=message.role)
        return message


    @staticmethod
    async def chat_completion_with_streaming(
        input_message: BaseMessage,
    ) -> StreamingResponse:
        subscription: openai.ChatCompletion = await openai.ChatCompletion.acreate(
            model=input_message.model,
            api_key=settings.OPENAI_API_KEY,
            messages=[{"role": ChatRolesEnum.USER.value, "content": input_message.message}],
            stream=True,
        )
        return StreamingResponse(stream_generator(subscription), media_type="text/event-stream")


    @staticmethod
    def extract_response_from_completion(chat_completion: ChatCompletion) -> str:
        return chat_completion.choices[0]["message"]["content"]
