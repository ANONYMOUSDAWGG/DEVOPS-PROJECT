from flask import Flask, jsonify, abort

app = Flask(__name__)

USERS = {
    1: {"id": 1, "name": "Aarav Shah", "email": "aarav@example.com"},
    2: {"id": 2, "name": "Priya Mehta", "email": "priya@example.com"},
    3: {"id": 3, "name": "Rohan Kulkarni", "email": "rohan@example.com"},
}


@app.route("/")
def home():
    return jsonify(service="user-service", status="running")


@app.route("/health")
def health():
    return jsonify(status="UP"), 200


@app.route("/users")
def get_users():
    return jsonify(list(USERS.values()))


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
