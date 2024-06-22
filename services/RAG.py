from pinecone.grpc import PineconeGRPC as Pinecone
import os
pc = Pinecone(api_key=os.environ.get("VECTOR_DB_API_KEY"))

class RAG:
    def __init__(self):
        self.db = pc.Index(name="pickpalette")
    def search(self,vectors):
        return self.db.query(vector=vectors,top_k=10,include_metadata=True)