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

    notes = db.relationship(
                        Note,
                        # The parameter Note defines the SQLAlchemy class that the Person class will be related to.
                        backref="person",
                        # A backwards reference in Note objects, each instance will contain an attribute called .person
                        cascade="all, delete, delete-orphan",
                        # This parameter tells SQLAlchemy to also delete all the Note instances associated with Person.
                        single_parent=True,
                        # SQLAlchemy not to allow an orphaned Note - instance without a parent Person object to exist.
                        order_by="desc(Note.timestamp)"
                        # SQLAlchemy desc() function will sort the notes in descending order (default is ascending)
    )
