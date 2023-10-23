from qdrant_client import QdrantClient

from app.chat.models import BaseMessage
from app.chat.exceptions import RetrievalNoDocumentsFoundExceptions
from settings import settings
from app.core.logs import logger

client =QdrantClient(settings.QDRANT_HOST, port=settings.QDRANT_PORT)

# ONLY FOR TEST PURPOSE (you may call this func by hand or let it be)


def process_retrieval(message: BaseMessage) -> BaseMessage:
    """ Search for given query using vector similarity search. If no documents are fund we raise an exception.
    If we do find documents we take the top 3 and put then into the context"""
    search_result = search(query=message.message)
    resulting_query: str = (
        f"Answer based only on context, nothing else. \n"
        f"QUERY:\n{message.message}\n"
        f"CONTEXT:\n{search_result}"
    )
    logger.info(f"Resulting Query: {resulting_query}")
    return BaseMessage(message=resulting_query, model=message.model)

def search(query: str) -> str:
    search_result = client.query(collection_name=settings.QDRANT_COLLECTION_NAME, limit=3, query_text=query)
    if not search_result:
        raise RetrievalNoDocumentsFoundExceptions
    return "\n".join(result.payload["page_content"] for result in search_result)