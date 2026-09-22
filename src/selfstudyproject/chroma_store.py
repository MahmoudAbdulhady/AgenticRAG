import chromadb

from langchain_chroma import Chroma

from .config import (
    CHROMA_API_KEY,
    CHROMA_TENANT,
    CHROMA_DATABASE,
    CHROMA_COLLECTION,
)

from .embeddings import get_embeddings


def get_chroma_client():
    return chromadb.CloudClient(
        api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE,
    )


def get_vector_store():
    client = get_chroma_client()

    return Chroma(
        client=client,
        collection_name=CHROMA_COLLECTION,
        embedding_function=get_embeddings(),
    )