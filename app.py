from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask app!, pokracuj na /heartbeat"


# This variable will store the latest heartbeat timestamp
latest_heartbeat = None
latest_heartbeat2 = None

@app.route('/heartbeat', methods=['POST', 'GET'])
def heartbeat():
    global latest_heartbeat

    if request.method == 'POST':
        # Capture the current time when the heartbeat is received
        latest_heartbeat = datetime.now().isoformat()
        data = request.json
        print("Received heartbeat data:", data)
        return jsonify(message="Heartbeat received", timestamp=latest_heartbeat, status=200), 200
    elif request.method == 'GET':
        if latest_heartbeat:
            return jsonify(message="App is running", last_heartbeat=latest_heartbeat, status=200), 200
        else:
            return jsonify(message="No heartbeat received yet", status=200), 200

@app.route('/heartbeat2', methods=['POST', 'GET'])
def heartbeat2():
    global latest_heartbeat2

    if request.method == 'POST':
        # Capture the current time when the heartbeat is received
        latest_heartbeat2 = datetime.now().isoformat()
        data = request.json
        print("Received heartbeat data:", data)
        return jsonify(message="Heartbeat received", timestamp=latest_heartbeat2, status=200), 200
    elif request.method == 'GET':
        if latest_heartbeat2:
            return jsonify(message="App is running", last_heartbeat=latest_heartbeat2, status=200), 200
        else:
            return jsonify(message="No heartbeat received yet", status=200), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
