from flask import Flask,request,jsonify
import json
import os
import time
from app_logger import logger

app = Flask(__name__)



default_data = {"name":"john doe", "age":30}
file_output = "output.json"
data_list = [{"id": 1, "data" : default_data}]


@app.before_request
def start_timer():
    request.start_time = time.time()
    logger.info(
        "Request Received",
        extra={
            "method": request.method,
            "url": request.url,
            "client_ip": request.remote_addr,
        }
    )

@app.after_request
def log_response(response):

   duration = round(time.time() - request.start_time, 3) if hasattr(request, "start_time") else -1
   
   logger.info(
        "Response sent",
        extra={
            "method": request.method,
            "url": request.path,
            "status_code": response.status_code,
            "duration": duration,
        }
    )
   
   return response

    
@app.route("/")
def welcome():

    if not os.path.exists(file_output):
        with open(file_output, "w") as file:
            json.dump(data_list, file)

    return " <h1> Hello World </h1> "

@app.route("/items/", methods=["GET"])
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
                "error" : "Your current list of Item",
            }), 400
    
@app.route("/items/<int:id>", methods=["GET"])
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

@app.route("/items/", methods=["POST"])
def post_response():
    if request.method == "POST":
        new_item = request.get_json()

        request

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
    
@app.route("/items/<int:id>", methods=["PUT"])
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


@app.route("/items/<int:id>", methods =['DELETE'])
def delete_data(id):

    if request.method == "DELETE":
        delete_status = False
        try:
            with open(file_output,"r") as file:
                curr_items = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):

            curr_items = []

        for item in curr_items:
            if item.get("id") == id:
                item.pop("id","data")
                delete_status = True
        
        if delete_status:
            with open(file_output,"w") as file:
                json.dump(curr_items,file,indent=4)
        
            return jsonify({
                    "message" : f"Successfully deleting data for id: {id}",
                    "data" : curr_items
                }), 200

        else:

            return jsonify({
                "error" : f"There's no match ID:{id}"
            }), 400

    else:
        return jsonify({"error": "Invalid format, please use JSON"}), 400    

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


