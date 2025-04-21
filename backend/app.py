from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/itinerary")
def itinerary():
    return jsonify({
        "day1": "台北 101 → 士林夜市",
        "day2": "九份 → 野柳地質公園",
        "day3": "台中彩虹眷村 → 逢甲夜市"
    })

if __name__ == "__main__":
    app.run(debug=True)
