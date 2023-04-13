# schemas.py

from config import db, ma
from models import Person, Note
from marshmallow_sqlalchemy import fields


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    notes = fields.Nested(NoteSchema, many=True)


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
