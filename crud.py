from flask import Flask, Blueprint,request, jsonify,current_app,g
import json
import os
import time
from auth import token_required
from logger import logger,logging

crud_blueprint = Blueprint("crud",__name__)

default_data = {"name":"john doe", "age":30}
file_output = "output.json"
data_list = [{"id": 1, "data" : default_data}]

#logging request/responses
@crud_blueprint.before_request
def start_timer():
    request.start_time = time.time()
    user_agent= request.headers.get("User-Agent")
    
    if current_app.debug:
        log_level = "DEBUG"
    else:
        log_level = "INFO"

    logger.log(
        getattr(logging, log_level),
        "Request Received",
        extra={
            "method": request.method,
            "url": request.url,
            "client_ip": request.remote_addr,
            "user-agent": user_agent.browser,
        }
    )

@crud_blueprint.after_request
def log_response(response):
    user_agent= request.headers.get("User-Agent")

    if hasattr(request, "start_time") :
        duration = round(time.time() - request.start_time, 3)
    else :
        duration = -1 

    if current_app.debug:
        log_level = "DEBUG"
    elif response.status_code < 400:
        log_level = "INFO"
    elif response.status_code < 500:
        log_level = "WARNING"
    else:
        log_level = "CRITICAL"


    logger.log(
        getattr(logging,log_level),
        "Response sent",
        extra={
            "method": request.method,
            "url": request.path,
            "status_code": response.status_code,
            "duration": f"{duration}s",
            "user-agent": user_agent.browser,
        }
    )

    return response

@crud_blueprint.route("/")
def welcome():

    if not os.path.exists(file_output):
        with open(file_output, "w") as file:
            json.dump(data_list, file)

    return " <h1> Hello World </h1> "



@crud_blueprint.route("/items/", methods=["GET"])
@token_required
def get_response():
    try:
        with open(file_output, "r") as file:
            items = json.load(file)
            return jsonify({
                "message" : "Your current list of Item",
                "data" : items
            }), 200

    except json.JSONDecodeError:
        return jsonify({
                "error" : "Error reading items list",
            }), 400
    
@crud_blueprint.route("/items/<int:id>", methods=["GET"])
def get_a_response(id):

    try:
        with open(file_output, "r") as file:
            items = json.load(file)
            
            for item in items:
                if item.get("id") == id:
                    return jsonify({
                        "message": f"Item with id : {id} found",
                        "data": item.get("data")
                    }), 200
            
            return jsonify({
                "error": f"Item with id : {id} not found"
            }), 404

    except json.JSONDecodeError:
        return jsonify({
            "error": "Error reading data"
        }), 400

@crud_blueprint.route("/items/", methods=["POST"])
def post_response():
    if request.method == "POST":
        new_item = request.get_json()

        try:
            with open(file_output, "r") as file:
                existing_data = json.load(file)

        except json.JSONDecodeError:
            existing_data = []

        if existing_data:
                    ids = [item.get("id") for item in existing_data if isinstance(item, dict) and "id" in item]
                    new_id = max(ids) + 1 if ids else 1


        new_item_with_id = {"id":new_id, "data": new_item}
        existing_data.append(new_item_with_id)

        with open(file_output,"w") as file:
            json.dump(existing_data, file, indent=2)

        return jsonify({
            "message": "new data added to the local JSON file", 
            "data" : new_item_with_id
            }), 201
    
    else:
        return jsonify({"error": "Invalid format, please use JSON"}), 400
    
@crud_blueprint.route("/items/<int:id>", methods=["PUT"])
def update_list(id):
    if request.method == "PUT":

        new_data = request.get_json()
        found = False

        try:
            with open(file_output, "r") as file:
                current_data = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            current_data = []

        for item in current_data:
                if item.get("id") == id:
                    item["data"] = new_data
                    found = True
                    break
        if found:
            with open(file_output, "w") as file:
                json.dump(current_data, file, indent=2)

            return jsonify({
                "message" : f"Successfully updating data for id: {id}",
                "data" : new_data
            }), 200

        else:

            return jsonify({
                "error" : f"There's no match ID:{id}"
            }), 400

    else:
        return jsonify({"error": "Invalid format, please use JSON"}), 400   


@crud_blueprint.route("/items/<int:id>", methods =['DELETE'])
def delete_data(id):

    if request.method == "DELETE":
        delete_status = False
        try:
            with open(file_output,"r") as file:
                current_data = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):

            current_data = []

        for item in current_data:
            if item.get("id") == id:
                item.pop("id","data")
                delete_status = True
        
        if delete_status:
            with open(file_output,"w") as file:
                json.dump(current_data,file,indent=4)
        
            return jsonify({
                    "message" : f"Successfully deleting data for id: {id}",
                    "data" : current_data
                }), 200

        else:

            return jsonify({
                "error" : f"There's no match ID:{id}"
            }), 400

    else:
        return jsonify({"error": "Invalid format, please use JSON"}), 400