# notes.py

from flask import abort, make_response

from config import db
from models import Person, Note
from schemas import note_schema


def create(note):
    personid = note.get("id_person")
    person = Person.query.get(personid)

    if person:
        new_note = note_schema.load(note, session=db.session)
        person.notes.append(new_note)
        db.session.commit()

        return note_schema.dump(new_note), 201
    else:
        abort(
            404,
            f"Person not found for ID: {personid}"
        )


def read_one(noteid):
    note = Note.query.get(noteid)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(
            404, f"Note with ID {noteid} not found"
        )


def update(noteid, note):
    existing_note = Note.query.get(noteid)

    if existing_note:
        update_note = note_schema.load(note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()

        return note_schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {noteid} not found")



def delete(noteid):
    existing_note = Note.query.get(noteid)

    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()

        return make_response(f"{noteid} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {noteid} not found")
