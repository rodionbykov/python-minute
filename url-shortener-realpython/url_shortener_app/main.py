import validators
import secrets

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import models, schema
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return "Hello world"


@app.get("/{url_key}")
def get_url_redirect(url_key: str, request: Request, db: Session = Depends(get_db)):
    db_url = (
            db
              .query(models.URL)
              .filter(models.URL.key == url_key, models.URL.is_active)
              .first()
              )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        HTTPException(status_code=404, detail="URL with key {url_key} not found")


@app.post("/", response_model=schema.URLInfo)
def create_url(url: schema.URLBase, db: Session = Depends(get_db)):

    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid target URL provided")
    key = get_secret_key("both", 5)
    secret_key = get_secret_key("upper", 8)

    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.pwd = secret_key
    db_url.clicks = 0

    return db_url


def get_secret_key(kind, len):
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
