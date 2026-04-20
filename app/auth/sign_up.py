"""Handles POST /auth/sign-up — registers a new user."""

from app.auth import auth_bp


@auth_bp.route("/sign-up", methods=["POST"])
def sign_up():
    # Implementation for sign-up logic
    return "sign-up successful"
