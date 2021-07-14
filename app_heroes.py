import flask
from flask import request, json, jsonify
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
# app.config['MYSQL_HOST'] = 'mysqlcontainer'

@app.route("/api", methods=["GET"])
def index():
    data = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
    return data.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")