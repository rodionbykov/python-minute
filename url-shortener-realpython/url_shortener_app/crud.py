from sqlalchemy.orm import Session

from . import helper, models, schema

def create_db_url(db: Session, url: schema.URLBase) -> models.URL:
    key = helper.create_unique_key()
    secret_key = f"{key}_{helper.get_secret_key('upper', 8)}"
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )

def get_db_url_by_secret_key(db: Session, url_secret_key: str) -> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.secret_key == url_secret_key, models.URL.is_active)
        .first()
    )
