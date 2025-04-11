from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
 
app = Flask(__name__)
 
# Azure OpenAI config
ENDPOINT = "https://mango-bush-0a9e12903.5.azurestaticapps.net/api/v1"
API_KEY = "4e49e4fb-bf76-47ae-b158-69028640aac6"
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4"
 
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# Directs to welcome page first 
@app.route("/")
def home():
    return render_template("welcome.html")

# Directs to chatbot page
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# Runs chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Empty message"}), 400
 
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system",
             "content": "You are a Key Stage 1 teacher who is trying to teach children basic literacy and math fundamentals as simple as possible. Only produce content that is appropriate for children of that age."},
            {"role": "user", "content": user_input}],
    )
 
    reply = response.choices[0].message.content.strip()
    return jsonify({"response": reply})
 
if __name__ == "__main__":
    app.run(debug=True)