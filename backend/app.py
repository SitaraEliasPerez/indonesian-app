from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # allows request from React dev server

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Selamat datang!"})

@app.route("/api/words")
def get_words():
    # Placeholder; will come from MySQL later
    words = [
        {"id": 1, "indonesian": "halo", "english": "hello"},
        {"id": 2, "indonesian": "terima kasih", "english": "thank you"}
    ]
    return jsonify(words)

if __name__ == "__main__":
    app.run(debug=True) # runs on localhost