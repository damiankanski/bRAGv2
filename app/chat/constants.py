from enum import StrEnum


# add type of possible errors
class FailureReasonsEnum(StrEnum):
    OPENAI_ERROR = "OpenAI call failed"
    STREAM_TIMEOUT = "Stream timed out"
    FAILED_PROCESSING = "Post processing failed"


# add basic roles as in article in LLM user system assistant
class ChatRolesEnum(StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"


# add chat version
class ModelsEnum(StrEnum):
    GPT4 = "gpt-4-0613"
