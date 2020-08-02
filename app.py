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
        latitude = 4
        longitude = 6
        obj = {
            "status" : 200,
        }
        return jsonify(obj)
    if request.method == 'GET':
        obj = {
            "latitude" : latitude,
        }
        return jsonify(obj)
    else:
        return 'NOT IMPLEMENTED', 501
