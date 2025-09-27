from flask import request,jsonify,Blueprint,g
import jwt
from functools import wraps
from datetime import datetime, timedelta
import os
import json

with open("private.pem", "r") as file:
    PRIVATE_KEY = file.read()

with open("public.pem", "r") as file:
    PUBLIC_KEY = file.read()

auth_blueprint=Blueprint("auth", __name__)

users_db = "users.json"
dummy_user =[{
    "id": 1,
    "user_id":"admin@example.com",
    "password": "admin",  
}]

# Creating token decorator
# jwt.encoding/decoding = (payload,key,algorithm)
def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({
                "message": "Authorization header is missing"
            }), 401
        
        try:
            # Check if the header starts with 'Bearer '
            if not auth_header.startswith('Bearer '):
                return jsonify({
                    "message": "Invalid token format. Must be 'Bearer <token>'"
                }), 401

            # Extract the actual token
            token = auth_header.split(' ')[1]
            decoded_data = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])

            # Using thread-safe global variable flask proivde
            g.user = {'user_id': decoded_data['user_id']}

        except jwt.ExpiredSignatureError:
            return jsonify({
                "message": "Token has expired"
            }), 401
        
        except jwt.InvalidTokenError:
            return jsonify({
                "message": "Token invalid"
            }), 401
        
        except Exception as e:
            return jsonify({
                "message" : "Token Invalid"
            }), 401
        
        return f(*args, **kwargs)
    
    return wrapper
        

# Genarating Token
def generate_token(user_id):
    token = jwt.encode({
        "user_id": user_id,
        "exp": datetime.now() + timedelta(hours=24)},
        PRIVATE_KEY, algorithm="RS256")
    
    return token


@auth_blueprint.route("/register", methods=["POST"])
def register_users():

    if not os.path.exists("users.json"):
        with open(users_db,"w") as file:
            json.dump(dummy_user,file)


    if request.method == "POST":
        new_user = request.get_json()
        user_id = new_user["user_id"]
        password = new_user["password"]
    
        try:
            with open(users_db,"r") as file:
                current_data= json.load(file)

        except json.JSONDecodeError:
            current_data = []

        if current_data:
                        ids = [item.get("id") for item in current_data if isinstance(item, dict) and "id" in item]
                        new_id = max(ids) + 1 if ids else 1
        
        
        # Check if user_id already exists
        for item in current_data:
            if item["user_id"] == user_id:
                return jsonify({
                    "message": "Use a different email, current one was already being used by another account"
                }), 409
    
        new_user_with_id = {"id": new_id, "user_id": user_id, "password": password}
        current_data.append(new_user_with_id)

        with open(users_db,"w") as file:
            json.dump(current_data,file, indent=2)

        return jsonify({
            "message":f"Register new user : {user_id} with id: {new_id}"
        }), 201
    else:
        return jsonify({
             "error": "Invalid format, please use JSON"}), 400

        
@auth_blueprint.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":

        data = request.get_json()
        user_id = data["user_id"]
        password = data["password"]
    
        try:
            with open(users_db,"r") as file:
                users = json.load(file)

        except json.JSONDecodeError:
            users = []

        for user in users:
            if user["user_id"] == user_id and user["password"] == password:

                token = generate_token(user_id)

                return jsonify({
                    "token": token }), 200
            
        return jsonify({
                    "error": "User has enter wrong credentials"}), 400
    else:
        return jsonify({
                    "error": "Invalid format, please use JSON"}),400


    
             



