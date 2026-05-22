import hashlib
import secrets
from jose import jwt
from datetime import datetime
from datetime import timedelta

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


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


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
