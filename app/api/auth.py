from flask import Blueprint, jsonify, request

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/register', methods=['POST'])
def api_register():
    # Your API logic for registration
    return jsonify(status="success", message="Registration complete.")

@api_blueprint.route('/api/login', methods=['POST'])
def api_login():
    # Your API logic for login
    return jsonify(status="success", message="Login successful.")