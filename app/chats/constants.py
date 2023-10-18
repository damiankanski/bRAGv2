from enum import StrEnum

class FailurereasonsEnum(StrEnum):
    OPENAI_ERROR = "OpenAI call failled00"
    STREAM_TIMEOUT = "Stream timed out"
    FAILED_PROCESSING = "Post processing failed"


class ChatRolesEnum(StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class ModelsEnum(StrEnum):
    GPT4 = "gpt-4-0613"