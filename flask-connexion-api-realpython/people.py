# people.py

from flask import abort, make_response
from config import db
from models import Person
from schemas import people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def read_one(lastname):
    person = Person.query.filter(Person.lastname == lastname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lastname} not found"
        )


def create(person):
    lastname = person.get("lastname")

    existing_person = Person.query.filter(Person.lastname == lastname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lastname} already exists",
        )


def update(lastname, person):
    existing_person = Person.query.filter(Person.lastname == lastname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.firstname = update_person.firstname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404, f"Person with last name {lastname} not found"
        )


def delete(lastname):
    existing_person = Person.query.filter(Person.lastname == lastname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lastname} successfully deleted", 200)
    else:
        abort(
            404, f"Person with last name {lastname} not found"
        )
