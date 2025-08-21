from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify("Hello, World!"), 200


@app.get("/users")
def get_users():
    users = [
        {
            "id": 1,
            "name": "Petr",
            "age": 20
        },
        {
            "id": 2,
            "name": "Ivan",
            "age": 42
        },
    ]
    return jsonify(users), 200


if __name__ == '__main__':
    app.run(debug=True)