# config.py

import pathlib
import connexion

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=basedir)

app = connexion_app.app

# sqlite
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"

# mysql - do replace username and password in connection string
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://<MYSQL_USERNAME>:<MYSQL_PASSWORD>@localhost:3306/test"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
