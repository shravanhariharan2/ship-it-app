from flask import Flask, request, jsonify
from flask_cors import CORS
import scraper

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "hello world"

@app.route("/api/item", methods=["GET"])
def get_item():
    item = request.args.get('item')
    days = request.args.get('days')
    items = scraper.get_items(item, days)
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)