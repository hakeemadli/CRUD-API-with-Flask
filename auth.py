from flask import request,jsonify,Blueprint
import jwt
from functools import wraps
from config import Config
from datetime import datetime, timedelta

auth_blueprint=Blueprint("auth", __name__)

# Creating token decorater
# jwt.encoding/decoding = (payload,key,algorithm)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({
                "message":"Token is missing"
            }), 401
        
        try:
            if token.startswith("Bearer "):
                token = token[7:]
            
            data = jwt.decode(token, Config.JWT_PRIVATE_KEY,algorithms=["RS256"])

            curr_user_id = data["user_id"]

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
        
        return f(curr_user_id, *args, **kwargs)
    
    return decorated
        

# Genarating Token
def generate_token(user_id):
    token = jwt.decode({
        "user_id": user_id,
        "exp": datetime.now() + timedelta(hours=24)},
        Config.JWT_PUBLIC_KEY, algorithms=["HS256"])
    
    return token


@auth_blueprint.route("/login", methods=["POST","GET"])
@token_required
def login():
    if request.method=="POST":
        data = request.get_data
        user_id =data["user_id"]
        password =data["password"]



