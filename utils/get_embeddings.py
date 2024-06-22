from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
import os
model="models/embedding-001"
def get_embeddings(data:str):
    embeddings = GoogleGenerativeAIEmbeddings(model=model)
    return embeddings.embed_query(data)