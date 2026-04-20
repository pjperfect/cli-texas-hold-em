"""
This file initializes the server package and imports the main app module. It serves as the entry point for the server-side application, allowing us to run the poker game in a web environment. The app module will contain the Flask application and route definitions for handling game interactions with clients.
"""

from flask import Flask
from app.db import prisma


def create_app():
    app = Flask(__name__)

    # Register blueprints for authentication routes, i.e., login and sign-up
    from app.auth import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
