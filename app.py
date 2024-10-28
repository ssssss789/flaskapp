from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
last_heartbeat = None

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    global last_heartbeat
    last_heartbeat = datetime.now()
    return jsonify({"status": "Heartbeat received", "timestamp": last_heartbeat.strftime("%Y-%m-%d %H:%M:%S")}), 200

@app.route('/heartbeat/check', methods=['GET'])
def check_heartbeat():
    if last_heartbeat:
        return jsonify({"last_heartbeat": last_heartbeat.strftime("%Y-%m-%d %H:%M:%S")}), 200
    else:
        return jsonify({"error": "No heartbeat received yet"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
