from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def get_name():
    """"method that GET's address and sends small JSON array with personal
    name

    :returns: JSON array with personal name
    """
    data_name = {
        "name": "Kyle_Janson"
                }
    return jsonify(data_name)


@app.route("/name/<name>", methods=["GET"])
def get_personal_name(name):
    """"method that GET's address and passes in any name that might be
    typed into URL

    :returns: JSON array with user input name
    """
    data_per_name = {
        "message": "Hello there {0}".format(name)
                    }
    return jsonify(data_per_name)


@app.route("/distance", methods=["POST"])
def get_distance():
    """"method that uses POST method to get POSTED data points and finds
    distance between the two points

    :returns: JSON array with distance as well as original two points
    """
    import math as mt
    r = request.get_json()
    first_point = r["a"]
    second_point = r["b"]
    run_horiz = 0
    run_horiz = second_point[0]-first_point[0]
    rise_vert = 0
    rise_vert = second_point[1] - first_point[1]
    dist_two_points = mt.sqrt(run_horiz ** 2 + rise_vert ** 2)
    return_dict = {
        "distance": "Distance: " + str(dist_two_points),
        "a": first_point,
        "b": second_point,
                  }
    return jsonify(return_dict), 200
# from ipython run r2 =
# requests.post("http://127.0.0.1:5000/distance",
# json={"a": [2,4], "b": [5,6]})
# and r2.json()
