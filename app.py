from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# This variable will store the latest heartbeat timestamp
latest_heartbeat = None

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
