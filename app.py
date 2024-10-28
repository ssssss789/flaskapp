from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask app!"

@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    return "App is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
