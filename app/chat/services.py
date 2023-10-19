import openai
from openai import ChatCompletion

from app.chat.constants import ChatRolesEnum
from app.chat.models import BaseMessage, Message
from app.core.logs import logger
from settings import settings

class OpenAIService:
    @classmethod
    async def chat_completion(cls, input_message: BaseMessage) -> Message:
        logger.info(f"Received the following completion: {input_message}")
        completion: openai.ChatCompletion = await openai.ChatCompletion.acreate(
            model=input_message.model,
            api_key=settings.OPENAI_API_KEY,
            messages=[{"role": ChatRolesEnum.ASSISTANT.value, "content": input_message.message}],
        )
        logger.info(f"Got the following response: {completion}")
        return Message(
            model=input_message.model,
            message=cls.extract_response_from_completion(completion),
            role=input_message.role,
        )

    @staticmethod
    def extract_response_from_completion(chat_completion: ChatCompletion) -> str:
        return chat_completion.choices[0]["message"]["content"]