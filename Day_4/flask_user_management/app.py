from flask import Flask, jsonify, request
from dotenv import load_dotenv
from models import db, User
import os



def create_app(app_config=None):
    """ Accoding flask documantation """
    app = Flask(__name__)

    # Get database URI from environment variables or use default
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///:memory:")

    if app_config:
        app.config.update(app_config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
    app.config["SQLALCHEMY_ECHO"] = True

    db.init_app(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return jsonify("Hello, World!"), 200


    @app.get("/users")
    def get_users():
        users_db = User.query.all()
        users = [
            {
                "id": user.id, 
                "username": user.username, 
                "email": user.email
            } 
            for user in users_db
        ]
        return jsonify(users), 200

    @app.post("/users")
    def add_user():
        data = request.json # the same as request.get_json()
        new_user = User(username=data["username"], email=data["email"])  # User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created with id={new_user.id}"}), 201

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)