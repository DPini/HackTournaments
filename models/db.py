from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = db.Column
