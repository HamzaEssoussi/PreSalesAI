import os
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict

class RAGService:
    def __init__(self):
        self.chroma_host = os.getenv("CHROMA_HOST", "localhost")
        self.chroma_port = int(os.getenv("CHROMA_PORT", "8001"))
        
        # Connexion à ChromaDB
        self.client = chromadb.HttpClient(
            host=self.chroma_host,
            port=self.chroma_port
        )
        
        # Fonction d'embedding avec nomic-embed-text via Ollama
        self.embedding_fn = embedding_functions.OllamaEmbeddingFunction(
            url="http://ollama:11434/api/embeddings",
            model_name="nomic-embed-text"
        )
        
        # Créer ou récupérer la collection
        self.collection = self.client.get_or_create_collection(
            name="presales_documents",
            embedding_function=self.embedding_fn
        )
    
    def index_document(self, doc_id: str, content: str, metadata: Dict = {}):
        """Indexe un document dans ChromaDB"""
        self.collection.upsert(
            ids=[doc_id],
            documents=[content],
            metadatas=[metadata]
        )
        return True
    
    def search(self, query: str, n_results: int = 5) -> List[str]:
        """Recherche les documents similaires"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results.get("documents", [[]])[0]
    
    def get_collection_info(self):
        return {
            "count": self.collection.count(),
            "name": self.collection.name
        }