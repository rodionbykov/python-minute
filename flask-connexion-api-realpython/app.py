# app.py

import config
from flask import render_template
from models import Person

app = config.connexion_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def index():
    people = Person.query.all()
    return render_template("index.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
