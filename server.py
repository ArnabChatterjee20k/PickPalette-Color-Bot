from flask import Flask , request
from flask_cors import CORS
from dotenv import load_dotenv
from utils.get_embeddings import get_embeddings
from services.RAG import RAG
from services.AI import AI

def get_palettes(query):

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

    return chat_response


app = Flask(__name__)
cors = CORS(app)

@app.post("/")
def generate():
    body = request.get_json()
    print(body)
    description = body.get("description")
    ans = get_palettes(description)
    return ans.get("palette",[])

if __name__ == "__main__":
    load_dotenv(".env")
    app.run(port=5000,debug=True)