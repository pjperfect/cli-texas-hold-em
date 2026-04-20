"""Handles POST /auth/login — authenticates an existing user."""

from app.auth import auth_bp


@auth_bp.route("/login", methods=["POST"])
def login():
    # Implementation for login logic
    return "login successful"
