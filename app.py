from flask import Flask,request,jsonify
from crud import crud_blueprint
from auth import auth_blueprint

app = Flask(__name__)

#register app route
app.register_blueprint(crud_blueprint)
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7000")


