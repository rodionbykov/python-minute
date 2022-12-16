import validators

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette.datastructures import URL

from . import crud, models, schema
from .database import SessionLocal, engine
from .config import get_settings

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
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        HTTPException(status_code=404, detail="URL with key {url_key} not found")


@app.post("/", response_model=schema.URLInfo)
def create_url(url: schema.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid target URL provided")

    db_url = crud.create_db_url(db, url)

    return get_admin_info(db_url)


@app.get("/admin/{url_secret_key}", name="admin", response_model=schema.URLInfo)
def get_url_admin(url_secret_key: str, request: Request, db: Session = Depends(get_db)):
    if db_url := crud.get_db_url_by_secret_key(db=db, url_secret_key=url_secret_key):
        return get_admin_info(db_url)
    else:
        HTTPException(status_code=404, detail="URL with secret key {url_secret_key} not found")


def get_admin_info(db_url: models.URL) -> schema.URLInfo:
    base_url = URL(get_settings().base_url)
    admin_endpoint = app.url_path_for("admin", url_secret_key=db_url.secret_key)
    db_url.url = str(base_url.replace(path=db_url.key))
    db_url.pwd = str(base_url.replace(path=admin_endpoint))
    db_url.clicks = 0

    return db_url
