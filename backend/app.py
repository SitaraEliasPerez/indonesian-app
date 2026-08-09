from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Word(db.Model):
    __tablename__ = "words"
    id         = db.Column(db.Integer, primary_key=True)
    category   = db.Column(db.String(50), nullable=False)
    indonesian = db.Column(db.String(100), nullable=False)
    english    = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id":          self.id,
            "category":    self.category,
            "indonesian":  self.indonesian,
            "english":     self.english,
        }

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Selamat datang!"})

@app.route("/api/words")
def get_words():
    words = Word.query.all()
    return jsonify([w.to_dict() for w in words])

@app.route("/api/words/<category>")
def get_words_by_category(category):
    words = Word.query.filter_by(category=category).all()
    return jsonify([w.to_dict() for w in words])

if __name__ == "__main__":
    app.run(debug=True)