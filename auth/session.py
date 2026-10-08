"""Session token validation for the sandbox auth surface."""
import hashlib
import hmac
import os

SECRET_KEY = os.environ.get("APP_SECRET_KEY", "dev-only-change-me")


def hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000).hex()


def verify_token(token: str, expected: str) -> bool:
    return hmac.compare_digest(token, expected)


def authenticate(username: str, password: str, stored_salt: str, stored_hash: str) -> bool:
    return hmac.compare_digest(hash_password(password, stored_salt), stored_hash)
