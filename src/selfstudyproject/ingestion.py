from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import UnstructuredLoader
from selfstudyproject.chroma_store import  get_vector_store
from .sources import sources


def load_documents():
    documents = []
    for source in sources:
        loader = UnstructuredLoader(web_url=source["url"])
        elements = loader.load()
        content = "\n\n".join(
            element.page_content.strip()
            for element in elements
            if element.page_content.strip()
        )

        document = Document(
            page_content=content,
            metadata={
                "source_name": source["name"],
                "source_url": source["url"],
            },
        )

        documents.append(document)
    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(documents)
    return chunks

def embed_documents():
    document = load_documents()
    print(f"Documents loaded: {len(document)}")
    chunks = split_documents(document)
    print(f"Created {len(chunks)} chunks")
    vector_store =  get_vector_store()
    print("Adding Documents to Chroma...")
    vector_store.add_documents(documents=chunks)
    print("Documents added to Chroma successfully")