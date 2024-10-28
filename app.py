from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/heartbeat', methods=['POST', 'GET'])
def heartbeat():
    if request.method == 'POST':
        # You can process the data sent in the POST request if needed
        data = request.json
        print("Received heartbeat data:", data)
        return jsonify(message="Heartbeat received", status=200), 200
    elif request.method == 'GET':
        return jsonify(message="App is running", status=200), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
