import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    database_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/cloudapp")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .models import Message

    @app.get("/")
    def home():
        return """
        <html>
        <head><title>S4 Cloud Web Application</title></head>
        <body>
        <h1>S4 Cloud Web Application</h1>
        <p>Flask + PostgreSQL + Docker + GitHub Actions</p>
        <p>Status: <strong>Running</strong></p>
        </body>
        </html>
        """

    @app.get("/health")
    def health():
        return {"status": "healthy", "service": "s4-cloud-web-application"}

    @app.get("/messages")
    def messages():
        return {"messages": [{"id": m.id, "message": m.message} for m in Message.query.all()]}

    with app.app_context():
        db.create_all()

    return app
