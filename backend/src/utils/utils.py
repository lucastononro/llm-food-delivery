
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, Document, ServiceContext

def load_pinecone_index(index_name, CONFIG):
    """Loads the pinecone index from the index_name"""

    vector_store = PineconeVectorStore(
        index_name=index_name,
        environment=CONFIG["pinecone"]["environment"],
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index = VectorStoreIndex([], storage_context=storage_context,)

    return index

def get_retriever(index_name: str, top_k:int,  CONFIG, **kwargs):
        """Returns a retriever object from a pinecone index"""

        # Loads the index
        index = load_pinecone_index(index_name, CONFIG)

        # Returns the retriever
        return index.as_retriever(similarity_top_k=top_k, **kwargs)
    