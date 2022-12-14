import validators

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import crud, models, schema
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
    if db_url:=  crud.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        HTTPException(status_code=404, detail="URL with key {url_key} not found")


@app.post("/", response_model=schema.URLInfo)
def create_url(url: schema.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid target URL provided")

    db_url = crud.create_db_url(db, url)
    db_url.url = db_url.key
    db_url.pwd = db_url.secret_key
    db_url.clicks = 0

    return db_url
