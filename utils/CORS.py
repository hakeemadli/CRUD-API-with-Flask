from flask import jsonify, request, g
from functools import wraps

def cors_header(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        
        if isinstance(response, tuple):
            response[0].headers["Access-Control-Allow-Origin"] = "*"
            
            # Handle tuple responses (data, status_code)
            response[0].headers['Access-Control-Allow-Origin'] = '*'
            response[0].headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response[0].headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            return response
        else:
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            return response
    return wrapper



    
