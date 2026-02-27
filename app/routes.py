from flask import Blueprint, request, jsonify, render_template
from .service import json_to_toon

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/toon', methods=['POST'])
def convert():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON provided"}), 400

    result = json_to_toon(data)
    return jsonify({"result": result})