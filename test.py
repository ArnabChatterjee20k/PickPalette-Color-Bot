from dotenv import load_dotenv
from utils.get_embeddings import get_embeddings
from services.RAG import RAG
from services.AI import AI

def main(query):
    load_dotenv(".env")

    rag = RAG()
    ai = AI()

    vectors = get_embeddings(query)

    try:
        results = rag.search(vectors)
        matches = results.to_dict().get("matches", [])
    except Exception as e:
        print(f"Error performing RAG search: {e}")
        return

    app_descriptions = []
    for app in matches:
        palettes = app.get("metadata", {}).get("palettes", [])
        app_descriptions.append(str(palettes))
    
    app_descriptions_str = "\n".join(app_descriptions)
    print("Collected app descriptions (palettes):")
    print(app_descriptions_str)


    chat_response = ai.chat(app_descpriptions=app_descriptions_str, description=query)
    print("\nAI Chat Response:")
    print(chat_response)

if __name__ == "__main__":
    main("A web app that helps users manage their expenses, income, and savings goals with an AI assistant to provide financial advice and answer questions.")