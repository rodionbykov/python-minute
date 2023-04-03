# models.py

from datetime import datetime
from config import db


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    id_person = db.Column(db.Integer, db.ForeignKey("people.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(32), unique=True)
    firstname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    notes = db.relationship(Note,
                            backref="people",
                            cascade="all, delete, delete-orphan",
                            single_parent=True,
                            order_by="desc(Note.timestamp)")
