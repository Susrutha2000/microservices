# order_service/app.py
from flask import Flask, jsonify
import requests  # <--- for calling another service

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:5001"  # Docker service name

@app.route("/orders/")
def orders():
    return jsonify([
        {"order_id": 101, "item": "Laptop"},
        {"order_id": 102, "item": "Phone"}
    ])

@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    return jsonify({
        "order_id": order_id,
        "items": ["item1", "item2"]
    })

@app.route("/orders-with-users")
def orders_with_users():
    # Call the user service
    response = requests.get(f"{USER_SERVICE_URL}/users")
    users = response.json()  # list of users

    # Example order data
    orders = [
        {"order_id": 101, "item": "Laptop", "user": users[0]},
        {"order_id": 102, "item": "Phone", "user": users[1]}
    ]

    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
