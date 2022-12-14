import secrets

from sqlalchemy.orm import Session

from . import crud


def get_secret_key(kind: str = "both", len: int = 5) -> str:
    charsLower = "abcdefghijklmnopqrstuvwxyz"
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if kind == "both":
        chars = charsLower + charsUpper
    if kind == "lower":
        chars = charsLower
    if kind == "upper":
        chars = charsUpper

    chars = chars + "1234567890"

    secret_key = "".join(secrets.choice(chars) for _ in range(len))

    return secret_key


def create_unique_key(db: Session) -> str:
    key = get_secret_key()
    while crud.get_db_url_by_key(db, key):
        key = get_secret_key()

    return key
