from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users/")
def users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com"
    })

if __name__ == "__main__":
    print("🔥 USER SERVICE STARTED 🔥")
    app.run(host="0.0.0.0", port=5001)
