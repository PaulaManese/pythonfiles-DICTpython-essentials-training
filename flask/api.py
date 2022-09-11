from flask import Flask, jsonify
from flights_data import flights
from utils import search_flight

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/flights")
def get_flights():
    return jsonify(flights)

@app.route("/flights/<int:id>")
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)
    # return str(id)

if __name__ == '__main__':
    app.run(debug=True)
