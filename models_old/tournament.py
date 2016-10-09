from db import db

class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    max_players_team(db.Integer)
    max_teams(db.Integer)
