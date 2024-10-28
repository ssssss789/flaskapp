from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask app!"

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.get_json()
    timestamp = data.get('timestamp')
    print(f"Received heartbeat at: {timestamp}")
    return jsonify(message="App is running"), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
