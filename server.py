from flask import Flask , request
from flask_cors import CORS
from dotenv import load_dotenv
from utils.ai_chat import ai_chat

app = Flask(__name__)
cors = CORS(app)

@app.post("/")
def generate():
    body = request.get_json()
    print(body)
    description = body.get("description")
    ans = ai_chat(description)
    return ans

if __name__ == "__main__":
    load_dotenv(".env")
    app.run(port=5000,debug=True)