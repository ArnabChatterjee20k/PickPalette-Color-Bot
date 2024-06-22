from utils.get_embeddings import get_embeddings
from services.RAG import RAG
from services.AI import AI

def ai_chat(query):

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
        app_descriptions.append(",".join(palettes))
    
    app_descriptions_str = "\n".join(app_descriptions)
    print("Collected app descriptions (palettes):")
    print(app_descriptions_str)


    chat_response = ai.chat(app_descpriptions=app_descriptions_str, description=query)
    print("\nAI Chat Response:")
    print(chat_response)

    return chat_response.get("palette",[])
