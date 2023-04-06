# notes.py

from flask import abort, make_response

from config import db
from models import Note
from schemas import note_schema


def read_one(noteid):
    note = Note.query.get(noteid)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(
            404, f"Note with ID {noteid} not found"
        )
