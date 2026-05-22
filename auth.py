import hashlib
import secrets


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000,
    ).hex()

    return f"{salt}${password_hash}"


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    try:
        salt, saved_hash = hashed_password.split("$", 1)
    except ValueError:
        return False

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        plain_password.encode(),
        salt.encode(),
        100000,
    ).hex()

    return secrets.compare_digest(password_hash, saved_hash)
