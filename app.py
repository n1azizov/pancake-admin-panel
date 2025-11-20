
from flask import Flask, jsonify, request, send_from_directory, session
import json, os

app = Flask(__name__)
app.secret_key = "CHANGE_ME"

USERS_FILE = "users.json"
ADMIN_USER = "admin"
ADMIN_PASS = "admin"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

@app.route("/")
def serve_login():
    return send_from_directory(".", "index.html")

@app.route("/admin")
def serve_admin():
    return send_from_directory(".", "admin.html")

@app.route("/page/<name>")
def serve_page(name):
    return send_from_directory("pages", f"{name}.html")

@app.route("/api/admin/login", methods=["POST"])
def admin_login():
    data = request.get_json()
    if data.get("username")==ADMIN_USER and data.get("password")==ADMIN_PASS:
        session["admin"]=True
        return jsonify({"message":"ok"})
    return jsonify({"error":"invalid"}),401

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(load_users())

@app.route("/api/users", methods=["POST"])
def add_user():
    if not session.get("admin"):
        return jsonify({"error":"not admin"}),401
    data = request.get_json()
    users = load_users()
    users.append(data)
    save_users(users)
    return jsonify({"message":"added"})

if __name__ == "__main__":
    app.run(debug=True)
