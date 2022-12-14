"""Models for Blogly."""


from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Site user"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   )
    first_name = db.Column(db.Text,
                           nullable=False,
                           )
    last_name = db.Column(db.Text,
                          nullable=False,
                          )
    image_url = db.Column(db.Text,
                          nullable=False,
                        #   default=DEFAULT_IMAGE_URL
                        )
