import os

from dotenv import load_dotenv


load_dotenv()


CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
CHROMA_TENANT = os.getenv("CHROMA_TENANT")
CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION")


if not CHROMA_API_KEY:
    raise ValueError("CHROMA_API_KEY is missing")

if not CHROMA_TENANT:
    raise ValueError("CHROMA_TENANT is missing")

if not CHROMA_DATABASE:
    raise ValueError("CHROMA_DATABASE is missing")

if not CHROMA_COLLECTION:
    raise ValueError("CHROMA_COLLECTION is missing")