from flask import Flask, jsonify, request, render_template
import json
app = Flask(__name__, template_folder='../Front-End')

latitude = 0
longitude = 0

@app.route("/location/coordinates", methods=['GET', 'POST'])
def storeCoordinates():
    global latitude
    global longitude
    if request.method == 'POST':
        # request must be a json with format:
        # {
        #     "latitude" : [value],
        #     "longitude" : [value]
        # }
        coordinates = request.json
        latitude = coordinates["latitude"]
        longitude = coordinates["longitude"]
        return 'OK', 200
    if request.method == 'GET':
        obj = {
            "latitude" : latitude,
            "longitude" : longitude,
        }
        return jsonify(obj)
    else:
        return 'NOT IMPLEMENTED', 501
