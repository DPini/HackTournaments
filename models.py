from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Tournament(db.Model):
    __tablename__ = "tournaments"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    max_players_team = db.Column(db.Integer)
    max_teams = db.Column(db.Integer)

class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tournament = db.Column(db.Integer,db.ForeignKey("tournaments.id"), nullable = False)
    name = db.Column(db.String(100))

    def get_teams_by_tournament(tournament):
        return Team.query.filter(Team.tournament == tournament)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

class Membership(db.Model):
    __tablename__ = "memberships"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    team = db.Column(db.Integer,db.ForeignKey("teams.id"), nullable = False)
    user = db.Column(db.Integer,db.ForeignKey("tournaments.id"), nullable = False)
