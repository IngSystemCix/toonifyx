from flask import Blueprint, request, jsonify
from .service import json_to_toon

main = Blueprint('main', __name__)

@main.route('/api/toon', methods=['POST'])
def convert():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON provided"}), 400

    result = json_to_toon(data)
    return jsonify({"result": result})